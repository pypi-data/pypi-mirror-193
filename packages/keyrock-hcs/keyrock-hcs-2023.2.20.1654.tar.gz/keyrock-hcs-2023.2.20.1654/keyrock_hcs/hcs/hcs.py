import json
import marshmallow as m
import logging
logger = logging.getLogger(__name__)

from keyrock_core import json_util

from .schema import TypeConfigFactory
from . import datastore
from . import settings
from . import exc


class HCS():
    class BaseSchema(m.Schema):
        class Meta:
            include = {
                'title': m.fields.String(required=True),
                'object_class': m.fields.String(required=True),
                'project_id': m.fields.Integer(missing=None),
                'parent_id': m.fields.Integer(missing=None),
            }

    class StoreSchema(BaseSchema):
        class Meta:
            include = {
                'settings_draft': m.fields.Dict(missing=None),
                'settings_published': m.fields.Dict(missing=None),
                'version_draft': m.fields.Integer(missing=0),
                'version_published': m.fields.Integer(missing=0),
            }

    class CacheSchema(BaseSchema):
        class Meta:
            include = {
                'settings': m.fields.Dict(required=True),
                'version': m.fields.Integer(required=True),
            }

    class EditorSchema(StoreSchema):
        class Meta:
            include = {
                'settings_tracked': m.fields.Dict(missing=None),
            }

    def __init__(self, type_map, src):
        # Factory for creating objects
        self.obj_factory = TypeConfigFactory(type_map)

        # Datastore for accessing raw obj data
        self.datastore = None
        self.cache = None
        if isinstance(src, dict):
            self.datastore = datastore.DictDatastore(src)
            self.cache = datastore.DictDatastore({})
        else:
            # TODO: Connection string for SQLAlchemy
            assert(False)

        # TODO: Have to clear the cache when the server comes online
        # or after recompile,
        # But don't want to do this every time an HCS object is created
        #self.cache.clear()

    def get_object_hcs(self, obj_id, default_type=None, published=True):
        if obj_id is None and default_type is None:
            raise Exception('type required for new object')

        object_merged = self.get_object_merged(obj_id, default_type=default_type, published=published)
        hcs_obj = self.obj_factory.get_instance(object_merged['object_class'], object_merged['settings'])
        hcs_obj.set_meta(obj_id=obj_id, title=object_merged['title'])

        #print('HCS OBJECT', hcs_obj)
        return hcs_obj

    def get_object_merged(self, obj_id, default_type=None, published=True):
        if not published:
            # If not published, have to build the merged object, but not save it
            object_merged = self.make_cache_object(obj_id, default_type, False)
            return object_merged

        object_merged = self.cache.get(obj_id, self.CacheSchema())
        if object_merged is None:
            # Build the merged object and save it
            object_merged = self.make_cache_object(obj_id, default_type, True)
            self.cache.set(obj_id, object_merged, self.CacheSchema())

        #print('MERGED OBJECT', json.dumps(object_merged, indent=2))
        return object_merged

    def make_cache_object(self, obj_id, default_type, published=True):
        object_raw = self.get_object_raw(obj_id, default_type=default_type)
        object_class = object_raw['object_class']

        if published:
            version = object_raw['version_published']
        else:
            version = object_raw['version_draft']

        settings_merged = self.get_settings_merged(obj_id, default_type=object_class)
        object_merged = HCS.CacheSchema().load({
            'object_class': object_class,
            'title': object_raw['title'],
            'project_id': object_raw['project_id'],
            'parent_id': object_raw['parent_id'],
            'settings': settings_merged,
            'version': version,
        })
        # TODO:
        # 2. Resolve ids to titles (project_id, parent_id) -> project_name
        # 3. Post process / cache object-specific transient data (dependency stuff?)
        return object_merged

    def get_object_raw(self, obj_id, default_type=None):
        if obj_id is None:
            # Fill out a new object
            # Use settings from default_type schema
            hcs_class = self.obj_factory.get_class(default_type)
            settings_default = hcs_class.ConfigSchema().load({})
            #print('DEFAULT SETTINGS', settings_default)
            obj_raw = self.StoreSchema().load({
                'title': 'Untitled',
                'object_class': default_type,
                'settings_published': settings_default,
            })
        else:
            obj_raw = self.datastore.get(obj_id, self.StoreSchema())
            if obj_raw is None:
                raise exc.ObjectNotFoundError(obj_id)

        #print('RAW OBJECT', obj_id, json.dumps(obj_raw, indent=2))
        return obj_raw

    def get_settings_merged(self, obj_id, default_type, published=True):
        settings_tracked = self.get_settings_tracked(obj_id, default_type=default_type, published=published)
        settings_merged = settings.tracked_to_local(settings_tracked)
        if settings_merged is None:
            settings_merged = {}
        return settings_merged

    def get_settings_tracked(self, obj_id, default_type, published=True, recursion_list=None):
        # Create the recursion list if it doesn't exist yet
        if recursion_list is None:
            recursion_list = []
        depth = len(recursion_list)

        local_obj = self.get_object_raw(obj_id, default_type)
        if local_obj['object_class'] != default_type:
            # This maybe doesn't need to be an error, could allow project-inheritance
            raise Exception("object_class mismatch: found '{0}' but expected '{1}'")

        if published:
            local_settings = local_obj['settings_published']
        else:
            local_settings = local_obj['settings_draft']

        if local_settings is None:
            local_settings = {}

        local_settings_tracked = settings.local_to_tracked(obj_id, local_settings, depth)

        parent_id = local_obj['parent_id']
        if obj_id in recursion_list:
            # Break the recursion
            parent_id = None
        else:
            recursion_list.append(obj_id)

        if obj_id is None and parent_id is None:
            # This is a default/root object and has no parent
            return local_settings_tracked

        parent_settings_tracked = self.get_settings_tracked(parent_id, default_type=default_type, published=True)
        merged_settings_tracked = settings.merge_tracked_settings(parent_settings_tracked, local_settings_tracked)
        return merged_settings_tracked

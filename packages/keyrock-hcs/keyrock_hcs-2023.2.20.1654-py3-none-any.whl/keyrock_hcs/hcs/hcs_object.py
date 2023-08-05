import marshmallow as m
import logging
logger = logging.getLogger(__name__)

from keyrock_core import hash_util


class HCSObject():
    class ConfigSchema(m.Schema):
        class Meta:
            include = {
                'is_hcs': m.fields.Boolean(missing=True),
                'empty_hack': m.fields.Boolean(required=False),
            }

    def __init__(self, config=None):
        if config is None:
            config = {}

        self.obj_id = None
        self.title = None

        # Validate the schema and load missing values
        self.config = self.ConfigSchema().load(config)
        self.config_hash = hash_util.get_dict_hash(self.config)
        self.load_config(self.config)

    def set_meta(self, obj_id=None, title=None):
        if obj_id is not None:
            self.obj_id = obj_id
        if title is not None:
            self.title = title

    def load_config(self, config):
        # Load config data onto the object for logic
        pass

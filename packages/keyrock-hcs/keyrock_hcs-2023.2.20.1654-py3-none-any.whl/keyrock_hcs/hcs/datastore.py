import json
import marshmallow as m

from . import schema
from . import exc


class Datastore():
    def __init__(self):
        pass

    def get(self, obj_id, schema):
        raise NotImplementedError()

    def set(self, obj_id, raw_data, schema):
        raise NotImplementedError()

    def clear(self):
        raise NotImplementedError()


class DictDatastore(Datastore):
    def __init__(self, obj_dict):
        super().__init__()
        self.obj_dict = obj_dict

    def get(self, obj_id, schema):
        raw_data = self.obj_dict.get(obj_id)
        if raw_data is None:
            return None
        return schema.load(raw_data)

    def set(self, obj_id, raw_data, schema):
        schema.validate(raw_data)
        if obj_id in self.obj_dict:
            self.obj_dict[obj_id].update(raw_data)
        else:
            self.obj_dict[obj_id] = raw_data

    def clear(self):
        self.obj_dict = {}


class PgDatastore(Datastore):
    # Maybe use SqlAlchemy to create the schema?
    def get(self, obj_id, schema):
        raise NotImplementedError()

    def set(self, obj_id, raw_data, schema):
        raise NotImplementedError()

    def clear(self):
        raise NotImplementedError()

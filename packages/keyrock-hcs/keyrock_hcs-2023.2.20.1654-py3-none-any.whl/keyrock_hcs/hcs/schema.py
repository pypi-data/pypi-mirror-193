import collections
from dataclasses import make_dataclass
import marshmallow as m


class DataClassSchema(m.Schema):
    @m.post_load
    def create_object(self, dict_val, **kwargs):
        class_name = type(self).__name__ + '_dataclass'
        obj = make_dataclass(class_name, [(k, type(v)) for k,v in dict_val.items()])
        for k, v in dict_val.items():
            setattr(obj, k, v)
        return obj


class TupleSchema(m.Schema):
    @m.post_load
    def create_namedtuple(self, dict_val, **kwargs):
        class_name = type(self).__name__ + '_tuple'
        keys = dict_val.keys()
        values = dict_val.values()
        return collections.namedtuple(class_name, keys)(*values)


class TypeConfigSchema(m.Schema):
    class Meta:
        include = {
            'type': m.fields.Str(missing='default'),
            'config': m.fields.Dict(missing={}),
        }


class TypeConfigFactory():
    def __init__(self, type_map):
        self.type_map = type_map

    def get_class(self, obj_type):
        inst_class = self.type_map.get(obj_type)
        if inst_class is None:
            raise Exception('type not found: {}'.format(type_config['type']))
        return inst_class

    def get_instance(self, obj_type, obj_config, **kwargs):
        inst_class = self.get_class(obj_type)
        return inst_class(obj_config, **kwargs)

    def from_type_config(self, type_config, **kwargs):
        if isinstance(type_config, str):
            type_config = {'type': type_config}

        inst_class = self.type_map.get(type_config['type'])
        if inst_class is None:
            raise Exception('type not found: {}'.format(type_config['type']))
        return inst_class(type_config.get('config', {}), **kwargs)

    def from_type_config_list(self, type_config_list, **kwargs):
        instance_list = []
        for type_config in type_config_list:
            instance_list.append(self.from_type_config(type_config, **kwargs))
        return instance_list

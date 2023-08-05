import unittest

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

from . import *


class TestSettings(unittest.TestCase):
    def test_merge(self):
        pass

    def test_tracking(self):
        pass


class TestHCSObject(unittest.TestCase):
    def test_constructor(self):
        test_obj = HCSObject()


# class TestHCS(unittest.TestCase):
#     def load_yaml(self, rel_path):
#         full_path = os.path.join(os.path.dirname(__file__), rel_path)
#         object_dict = None
#         with open(full_path, 'r') as f:
#             raw_txt = f.read()
#             object_dict = yaml.safe_load(raw_txt)
#         return object_dict

#     def test_inheritance(self):
#         type_map = {
#             'constant': distribution.Constant,
#             'uniform': distribution.Uniform,
#             'logistic': distribution.Logistic,
#             'normal': distribution.Normal,
#             'skew_normal': distribution.SkewNormal,
#             'log_normal': distribution.LogNormal,
#             'beta': distribution.Beta,
#             'gamma': distribution.Gamma,
#         }
#         object_dict = self.load_yaml('test_data/example_dist_obj.yml')

#         hcs_api = HCS(type_map, object_dict)

#         obj2 = hcs_api.get_object_hcs(2)
#         self.assertAlmostEqual(obj2.config['loc'], 10)
#         self.assertAlmostEqual(obj2.config['scale'], 2)

#         # TODO: Test inheritance class mismatches?
#         # Or... allow class mismatches (like for projects)

#     def test_cache(self):
#         pass

#     def test_draft_vs_published(self):
#         pass

#     def test_save(self):
#         pass
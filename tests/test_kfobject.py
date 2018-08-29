import unittest
from decimal import Decimal
from pykashflowapi.kfobjects.kfobject import KfObject


class SampleKfObject(KfObject):
    _items = {
        'boolean': False,
        'integer': 0,
        'string': '',
        'float': 0.0,
        'decimal': Decimal(0),
        'list': []
    }


class TestKfObject(unittest.TestCase):

    def test_setting_not_existing_key(self):
        kf_obj = KfObject()
        with self.assertRaises(KeyError):
            kf_obj['a'] = True

    def test_init_with_not_existing_key(self):
        with self.assertRaises(KeyError):
            KfObject({'a': True})

    def test_init_with_dict(self):
        sample_kf_obj = SampleKfObject({'boolean': True})
        self.assertTrue(sample_kf_obj.get('boolean', False))

    def test_getting_unset_item(self):
        sample_kf_obj = SampleKfObject()
        with self.assertRaises(KeyError):
            t = sample_kf_obj['boolean']

    def test_set_wrong_type(self):
        sample_kf_obj = SampleKfObject()
        with self.assertRaises(ValueError):
            sample_kf_obj['boolean'] = 0

    def test_set_wrong_type_on_init(self):
        with self.assertRaises(ValueError):
            SampleKfObject({'boolean': 0})

    def test_type_boolean(self):
        sample_kf_obj = SampleKfObject({'boolean': True})
        self.assertIsInstance(sample_kf_obj['boolean'], bool)

    def test_type_integer(self):
        sample_kf_obj = SampleKfObject({'integer': 1})
        self.assertIsInstance(sample_kf_obj['integer'], int)

    def test_type_string(self):
        sample_kf_obj = SampleKfObject({'string': ''})
        self.assertIsInstance(sample_kf_obj['string'], str)

    def test_type_float(self):
        sample_kf_obj = SampleKfObject({'float': 0.1})
        self.assertIsInstance(sample_kf_obj['float'], float)

    def test_type_decimal(self):
        sample_kf_obj = SampleKfObject({'decimal': Decimal(0)})
        self.assertIsInstance(sample_kf_obj['decimal'], Decimal)

    def test_type_list(self):
        sample_kf_obj = SampleKfObject({'list': []})
        self.assertIsInstance(sample_kf_obj['list'], list)


if __name__ == '__main__':
    unittest.main()

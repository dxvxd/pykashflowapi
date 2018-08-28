import unittest
from pykashflowapi.soapservice import KashflowSoapService


class TestKashflowSoapService(unittest.TestCase):

    def test_soapservice_init_username(self):
        service = KashflowSoapService('u', 'p')
        self.assertEqual('u', service.params['UserName'])

    def test_soapservice_init_password(self):
        service = KashflowSoapService('u', 'p')
        self.assertEqual('p', service.params['Password'])

    def test_add_to_params(self):
        service = KashflowSoapService('u', 'p')
        params = service._add_to_params({'a': 1})
        self.assertDictEqual({'UserName': 'u', 'Password': 'p', 'a': 1}, params)

import unittest
from pykashflowapi.kfobjects.kfobject import KfObject
from pykashflowapi.kfobjects.invoice import KfInvoice, KfInvoiceLine


class TestKfInvoice(unittest.TestCase):

    def test_invoice_is_kfobject(self):
        kf_invoice = KfInvoice()
        self.assertIsInstance(kf_invoice, KfObject)

    def test_invoice_line_is_kfobject(self):
        kf_invoice_line = KfInvoiceLine()
        self.assertIsInstance(kf_invoice_line, KfObject)

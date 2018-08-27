import unittest
from decimal import Decimal
from pykashflowapi.kfobjects.kfobject import KfObject
from pykashflowapi.kfobjects.invoice import KfInvoice, KfInvoiceLine


class TestKfInvoice(unittest.TestCase):

    def test_invoice_is_kfobject(self):
        kf_invoice = KfInvoice()
        self.assertIsInstance(kf_invoice, KfObject)

    def test_add_line_with_no_values(self):
        kf_invoice = KfInvoice({'Lines': [], 'NetAmount': Decimal(0), 'VATAmount': Decimal(0)})
        with self.assertRaises(KeyError):
            kf_invoice.add_line(KfInvoiceLine({}))

    def test_add_line_sort(self):
        kf_invoice = KfInvoice({'Lines': [], 'NetAmount': Decimal(0), 'VATAmount': Decimal(0)})
        kf_line = KfInvoiceLine({'Sort': 0, 'Rate': Decimal(0), 'Quantity': Decimal(0), 'VatAmount': Decimal(0)})
        kf_invoice.add_line(kf_line)
        self.assertEqual(1, kf_line['Sort'])

    def test_add_line_vat_sum(self):
        kf_invoice = KfInvoice({'Lines': [], 'NetAmount': Decimal(0), 'VATAmount': Decimal(0)})
        kf_line1 = KfInvoiceLine({'Sort': 0, 'Rate': Decimal(0), 'Quantity': Decimal(0), 'VatAmount': Decimal(10.3)})
        kf_line2 = KfInvoiceLine({'Sort': 0, 'Rate': Decimal(0), 'Quantity': Decimal(0), 'VatAmount': Decimal(11.0)})
        kf_invoice.add_line(kf_line1)
        kf_invoice.add_line(kf_line2)
        self.assertAlmostEqual(Decimal(21.3), kf_invoice['VATAmount'])

    def test_add_line_net_sum(self):
        kf_invoice = KfInvoice({'Lines': [], 'NetAmount': Decimal(0), 'VATAmount': Decimal(0)})
        kf_line1 = KfInvoiceLine({'Sort': 0, 'Rate': Decimal(2), 'Quantity': Decimal(2), 'VatAmount': Decimal(10.3)})
        kf_line2 = KfInvoiceLine({'Sort': 0, 'Rate': Decimal(3), 'Quantity': Decimal(3), 'VatAmount': Decimal(11.0)})
        kf_invoice.add_line(kf_line1)
        kf_invoice.add_line(kf_line2)
        self.assertAlmostEqual(Decimal(13), kf_invoice['NetAmount'])

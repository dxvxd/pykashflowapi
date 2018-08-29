from decimal import Decimal
from .kfobject import KfObject


class KfInvoiceLine(KfObject):
    _items = {
        "LineID": 0,  # Integer
        "Quantity": Decimal(0),  # Decimal
        "Description": '',  # String
        "Rate": Decimal(0),  # Decimal
        "ChargeType": 0,  # The ID of the nominal code assigned to the line item
        "ProjID": 0,  # If a Project is associated with the line item then the Project ID, else 0
        "VatAmount": Decimal(0),  # Decimal
        "VatRate": Decimal(0),  # The VAT rate for the line item. If 'N/A' (VAT exempt) declare a rate of -1
        "Sort": 0,  # The index of the line item for the document, starting from 1
        "ProductID": 0,  # If a Product of the ChargeType is declared then the Product ID, else 0
        "ValuesInCurrency": 0  # If the document is in a foreign currency and you are passing
                               # the Rate and VatAmount values in that currency then 1, else 0
    }

    def get_net(self):
        return self['Rate'] * self['Quantity']


class KfInvoice(KfObject):
    _items = {
        "InvoiceNumber": 0,  # Unsigned Integer
        "InvoiceDate": '',  # The issue date for the document in the ISO 8601 format of yyyy-mm-ddTHH:MM:SS
        "DueDate": '',  # The due date for the document in the ISO 8601 format of yyyy-mm-ddTHH:MM:SS
        "CustomerID": 0,  # Integer
        "NetAmount": Decimal(0),  # Decimal - The sum of the net value for all documents lines
        "VATAmount": Decimal(0),  # Decimal - The sum of the VAT value for all documents lines
        "Lines": [],  # Array of InvoiceLine objects

        "InvoiceDBID": 0,
        "Paid": 0,
        "SuppressTotal": 0,
        "ProjectID": 0,
        "ExchangeRate": 0,
        "AmountPaid": 0,
        "UseCustomDeliveryAddress": False,
    }

    def add_line(self, line):
        self['Lines'].append(line)
        self['NetAmount'] += line.get_net()
        self['VATAmount'] += line['VatAmount']
        line['Sort'] = len(self['Lines'])

from decimal import Decimal
from .kfobject import KfObject


class KfInvoiceLine(KfObject):
    _items = {
        "LineID": int,  # Integer
        "Quantity": Decimal,  # Decimal
        "Description": str,  # String
        "Rate": Decimal,  # Decimal
        "ChargeType": int,  # The ID of the nominal code assigned to the line item
        "ProjID": int,  # If a Project is associated with the line item then the Project ID, else 0
        "VatAmount": Decimal,  # Decimal
        "VatRate": Decimal,  # The VAT rate for the line item. If 'N/A' (VAT exempt) declare a rate of -1
        "Sort": int,  # The index of the line item for the document, starting from 1
        "ProductID": int,  # If a Product of the ChargeType is declared then the Product ID, else 0
        "ValuesInCurrency": int  # If the document is in a foreign currency and you are passing
                                 # the Rate and VatAmount values in that currency then 1, else 0
    }

    def get_net(self):
        return self['Rate'] * self['Quantity']


class KfInvoice(KfObject):
    _items = {
        "InvoiceNumber": int,  # Unsigned Integer
        "InvoiceDate": str,  # The issue date for the document in the ISO 8601 format of yyyy-mm-ddTHH:MM:SS
        "DueDate": str,  # The due date for the document in the ISO 8601 format of yyyy-mm-ddTHH:MM:SS
        "CustomerID": int,  # Integer
        "NetAmount": Decimal,  # Decimal - The sum of the net value for all documents lines
        "VATAmount": Decimal,  # Decimal - The sum of the VAT value for all documents lines
        "Lines": list,  # Array of InvoiceLine objects

        "InvoiceDBID": int,
        "Paid": int,
        "SuppressTotal": int,
        "ProjectID": int,
        "ExchangeRate": int,
        "AmountPaid": int,
        "UseCustomDeliveryAddress": bool,
    }

    def add_line(self, line):
        self['Lines'].append(line)
        self['NetAmount'] += line.get_net()
        self['VATAmount'] += line['VatAmount']
        line['Sort'] = len(self['Lines'])

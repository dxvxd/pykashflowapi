from decimal import Decimal
from .kfobject import KfObject


class KfInvoiceLine(KfObject):
    _items = {
        "LineID": 0,  # The system-wide, unique ID number for the nominal code (immutable)
        "Quantity": Decimal(0),  # The number representing how many of the item has been issued
        "Description": '',  # A string of free text for the line item
        "Rate": Decimal(0),  # The net value of a single item (ie the value of Quantity 1)
        "ChargeType": 0,  # The ID of the nominal code assigned to the line item
        "ProjID": 0,  # If a Project is associated with the line item then the Project ID, else 0
        "VatAmount": Decimal(0),  # The gross VAT amount for the line item
        "VatRate": Decimal(0),  # The VAT rate for the line item. If 'N/A' (VAT exempt) declare a rate of -1
        "Sort": 0,  # The index of the line item for the document, starting from 1
        "ProductID": 0,  # If a Product of the ChargeType is declared then the Product ID, else 0
        "ValuesInCurrency": 0  # If the document is in a foreign currency and you are passing
                               # the Rate and VatAmount values in that currency then 1, else 0
    }


class KfInvoice(KfObject):
    _items = {
        "InvoiceDBID": 0,  # The system-wide, unique ID number for this document (immutable)
        "InvoiceNumber": 0,  # The document number, must be unique for the KashFlow account for this document-type
        "InvoiceDate": '',  # The issue date for the document in the ISO 8601 format of yyyy-mm-ddTHH:MM:SS
        "DueDate": '',  # The due date for the document in the ISO 8601 format of yyyy-mm-ddTHH:MM:SS
        "SuppressTotal": 0,  # If the document is a Quote and the total is to be hidden then 1, else 0
        "ProjectID": 0,  # If a Project is associated with the document then the ProjectID, else 0
        "ExchangeRate": 0,  # The exchange rate for the defined currency
        "Paid": 0,  # If the document is an Invoice or Receipt and is completely paid then 1, else 0
        "CustomerID": 0,  # If an Invoice or Quote then the CustomerID, else the SupplierID
        "NetAmount": Decimal(0),  # The sum of the net value for all documents lines (read-only)
        "VATAmount": Decimal(0),  # The sum of the VAT value for all documents lines (read-only)
        "AmountPaid": 0,  # If the document is an Invoice or Purchase
                          # then the sum of all the payments made to it(read-only)
        "UseCustomDeliveryAddress": False,  # If the document is a Quote or Invoice and a Delivery Address is
                                            # defined to be used then true, else false
        "Lines": [],  # Array of InvoiceLine objects
    }
    _additional_items = {
        "CurrencyCode": '',  # The currency code in the ISO 4217 standard
        "CustomerReference": '',  # A string of free-text
        "EstimateCategory": '',  # If a Quote then it’s category (read-only)
        "Permalink": '',  # A permanent link to access a PDF of the document (read-only)
        "DeliveryAddress": {}  # An object of type DeliveryAddress
    }

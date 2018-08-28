from decimal import Decimal
from datetime import date
from .kfobject import KfObject


class KfCustomer(KfObject):
    _items = {
        "CustomerID": 0,  # The system-wide, unique ID number for the customer (immutable)
        "Code": '',  # An alphanumeric ID for the customer, unique for the KashFlow account customers list
        "Name": '',  # The name of the customer
        "Email": '',  # The customer email address(es)
        "EC": 0,  # If the customer is VAT Registered in another EC Member State then 1, else 0
        "OutsideEC": 0,  # If the customer is VAT Registered outside of the EC then 1, else 0
        "Source": 0,  # The ID for the source assigned to the customer
        "Discount": Decimal(0),  # The discount percentage for this customer
        "ShowDiscount": False,  # If the customer is specified to receive a discount then true, else false
        "PaymentTerms": 7,  # The number of days used to define the Due Date on Invoices from the Issue Date
        "CheckBox1": 0,  # Custom additional checkbox 1. If checked 1, else 0
        "CheckBox2": 0,
        "CheckBox3": 0,
        "CheckBox4": 0,
        "CheckBox5": 0,
        "CheckBox6": 0,
        "CheckBox7": 0,
        "CheckBox8": 0,
        "CheckBox9": 0,
        "CheckBox10": 0,
        "CheckBox11": 0,
        "CheckBox12": 0,
        "CheckBox13": 0,
        "CheckBox14": 0,
        "CheckBox15": 0,
        "CheckBox16": 0,
        "CheckBox17": 0,
        "CheckBox18": 0,
        "CheckBox19": 0,
        "CheckBox20": 0,
        "Created": date.today(),  # The date this customer record was inserted (immutable)
        "Updated": date.today(),  # The date this customer record was last updated (read-only?)
        "CurrencyID": 0,  # The ID for the customers default currency
    }

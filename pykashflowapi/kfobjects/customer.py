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
    _additional_items = {
        'Contact': '',  # The full contact name for the customer
        'Telephone': '',  # The customer telephone number
        'Mobile': '',  # The customer mobile number
        'Fax': '',  # The customer fax number
        'Address1': '',  # The customer billing address line 1
        'Address2': '',  # The customer billing address line 2
        'Address3': '',  # The customer billing address line 3
        'Address4': '',  # The customer billing address line 4
        'CountryName': '',  # The customer billing address country name
        'CountryCode': '',  # The customer billing address country code in the ISO 3166-1 alpha-2 standard
                            # (except for Greece which is recorded as ‘EL’)
        'Postcode': '',  # The customer billing address postcode
        'Website': '',  # The customer website URI
        'Notes': '',  # A string of additional free-text
        'ExtraText1': '',  # Custom additional text field 1
        'ExtraText2': '',  # Custom additional text field 2
        'ExtraText3': '',  # Custom additional text field 3
        'ExtraText4': '',  # Custom additional text field 4
        'ExtraText5': '',  # Custom additional text field 5
        'ExtraText6': '',  # Custom additional text field 6
        'ExtraText7': '',  # Custom additional text field 7
        'ExtraText8': '',  # Custom additional text field 8
        'ExtraText9': '',  # Custom additional text field 9
        'ExtraText10': '',  # Custom additional text field 10
        'ExtraText11': '',  # Custom additional text field 11
        'ExtraText12': '',  # Custom additional text field 12
        'ExtraText13': '',  # Custom additional text field 13
        'ExtraText14': '',  # Custom additional text field 14
        'ExtraText15': '',  # Custom additional text field 15
        'ExtraText16': '',  # Custom additional text field 16
        'ExtraText17': '',  # Custom additional text field 17
        'ExtraText18': '',  # Custom additional text field 18
        'ExtraText19': '',  # Custom additional text field 19
        'ExtraText20': '',  # Custom additional text field 20
        'ContactTitle': '',  # The customer contacts title
        'ContactFirstName': '',  # The customer contacts first name
        'ContactLastName': '',  # The customer contacts last name
        'CustHasDeliveryAddress': 0,  # If the customer is specified as having a delivery address separate to
                                      # their billing address then 1, else 0
        'DeliveryAddress1': '',  # The customer delivery address line 1
        'DeliveryAddress2': '',  # The customer delivery address line 2
        'DeliveryAddress3': '',  # The customer delivery address line 3
        'DeliveryAddress4': '',  # The customer delivery address line 4
        'DeliveryCountryName': '',  # The customer delivery address country name
        'DeliveryCountryCode': '',  # The customer delivery address country code in the ISO 3166-1 alpha-2 standard
                                    # (except for Greece which is recorded as ‘EL’)
        'DeliveryPostcode': '',  # The customer delivery address post code
        'VATNumber': '',  # The customer VAT number
    }

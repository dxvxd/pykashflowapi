from .soapservice import KashflowSoapService
from .exceptions import KashflowSoapException, KashflowException


class Kashflow:

    def __init__(self, username, password):
        self.service = KashflowSoapService(username, password)
        self.response = None

    def _handle_response(self, ):
        if self.response['Status'] != 'OK':
            raise KashflowSoapException(self.response['StatusDetail'])
        return self.response

    def _call_method(self, name, params=None):
        self.response = self.service.call_method(name, params)
        self._handle_response()

        return self.response[name + 'Result']

    def auth(self, auth_key, app_name):
        return self._call_method('AutoAuthIP', {'appName': app_name, 'AutoAuthKey': auth_key})

    def insert_invoice(self, invoice):
        return self._call_method('InsertInvoice', {'Inv': invoice})

    def insert_invoice_line_with_invoice_number(self, invoice_no, line):
        return self._call_method('InsertInvoiceLineWithInvoiceNumber', {'InvoiceNumber': invoice_no, 'InvLine': line})

    def get_account_overview(self):
        return self._call_method('GetAccountOverview')

    def get_customer_sources(self):
        return self._call_method('GetCustomerSources')

    def get_customers(self):
        return self._call_method('GetCustomers')

    def get_customer_by_email(self, email):
        return self._call_method('GetCustomerByEmail', {'CustomerEmail': email})

    def get_customer_by_code(self, code):
        return self._call_method('GetCustomer', {'CustomerCode': code})

    def insert_customer(self, customer):
        return self._call_method('InsertCustomer', {'custr': customer})

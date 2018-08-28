from zeep import Client


class KashflowSoapService:
    api_client = Client('https://securedwebapp.com/api/service.asmx?WSDL')
    params = {}

    def __init__(self, username, password):
        self.params['UserName'] = username
        self.params['Password'] = password

    def _add_to_params(self, params=None):
        kwargs = {}
        kwargs.update(self.params)
        if params:
            kwargs.update(params)
        return kwargs

    def call_method(self, name, params):
        kwargs = self._add_to_params(params)
        return getattr(self.api_client.service, name)(**kwargs)

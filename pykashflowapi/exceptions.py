
class KashflowException(Exception):
    details = None

    def __init__(self, details):
        self.details = details


class KashflowSoapException(KashflowException):
    pass

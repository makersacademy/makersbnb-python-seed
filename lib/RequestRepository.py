from lib.Request import Request

class RequestRepository:
    def __init__(self, connection):
        self._connection = connection
from util.util import timestamp_now
class BaseHandler:

    def __init__(self,name):
        self.handler_name = name

    def to_api_response(self,data):
        return {
            "timestamp":timestamp_now(),
            "data":data
        }

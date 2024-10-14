from django.utils.deprecation import MiddlewareMixin

class RequestCounterMiddleware(MiddlewareMixin):
    request_count = 0

    def process_request(self, request):
        RequestCounterMiddleware.request_count += 1

    @classmethod
    def get_request_count(cls):
        return cls.request_count

    @classmethod
    def reset_request_count(cls):
        cls.request_count = 0

from rest_framework.routers import SimpleRouter


class ApiRouter(object):

    def __init__(self):
        self.patterns = []

    def register(self, patterns):
        self.patterns.extend(patterns)

    @property
    def urls(self):
        router = SimpleRouter()
        for args in self.patterns:
            router.register(*args)
        return router.urls

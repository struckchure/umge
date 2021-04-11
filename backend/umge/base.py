from rest_framework.generics import GenericAPIView


class BaseAPIView(GenericAPIView):

    context = {}

    def get_context(self):
        return self.context

    def set_context(self, key, value):
        self.context[key] = value

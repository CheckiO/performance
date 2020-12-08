from django.contrib.auth.models import User

from rest_framework import mixins, status, exceptions
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from apps.profiles.api import serializers


class CurrentUsersViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            serializer = serializers.AnonymousUserSerializer()
        else:
            serializer = serializers.CurrentUserSerializer(instance=instance)
        return Response(serializer.data)

    def get_object(self):
        user = self.request.user
        if user.is_authenticated:
            return self.request.user
        return None

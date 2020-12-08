from django.contrib.auth.models import User

from rest_framework import serializers


class AnonymousUserSerializer(serializers.Serializer):
    is_authenticated = serializers.CharField(initial=False)


class CurrentUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField(source='pk')
    username = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('id', 'username')

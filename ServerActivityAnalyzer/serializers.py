from rest_framework import serializers

from .models import (
    ServerResponse,
    Server
)


class ServerResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerResponse
        fields = ('response_from', 'response_time', 'created_at')


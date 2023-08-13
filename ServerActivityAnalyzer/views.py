from rest_framework import mixins, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ServerActivityAnalyzer.models import Server
from ServerActivityAnalyzer.serializers import ServerSerializer


class ServersViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from ServerActivityAnalyzer.controllers import ServersChartController


class ServersChartViewSet(viewsets.ViewSet):
    def list(self, request):
        data = ServersChartController.get_chart_data()
        return Response(data)

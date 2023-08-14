from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ServerActivityAnalyzer.views import ServersChartViewSet

router = DefaultRouter()
router.register(r'server-chart', ServersChartViewSet, basename='server-chart')


urlpatterns = [
    path('', include(router.urls)),
]

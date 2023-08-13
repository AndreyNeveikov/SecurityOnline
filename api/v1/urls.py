from rest_framework.routers import DefaultRouter

from ServerActivityAnalyzer.views import ServersViewSet

router = DefaultRouter()
router.register(r'server', ServersViewSet, basename='server')

urlpatterns = router.urls

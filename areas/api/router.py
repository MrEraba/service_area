from rest_framework.routers import DefaultRouter

from areas.api.views import ServiceAreaViewSet

router = DefaultRouter()
router.register('areas', ServiceAreaViewSet)

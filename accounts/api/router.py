from rest_framework import routers

from accounts.api.views import UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
from rest_framework.throttling import UserRateThrottle
from rest_framework.viewsets import ModelViewSet

from .filters import PointFilter
from .serializers import AreaSerializer
from ..models import Area


class ServiceAreaViewSet(ModelViewSet):
    serializer_class = AreaSerializer
    queryset = Area.objects.all()
    throttle_classes = [UserRateThrottle]
    filter_backends = [PointFilter]


from rest_framework import viewsets

from .serializers import ProviderSerializer
from ..models import Provider


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

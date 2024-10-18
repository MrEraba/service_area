from rest_framework import serializers
from rest_framework_gis.serializers import Polygon

from ..models import Area


class AreaSerializer(serializers.HyperlinkedModelSerializer):
    region = Polygon()

    class Meta:
        model = Area
        fields = ['id', 'name', 'region', 'owner', 'url']

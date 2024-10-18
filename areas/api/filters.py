from django.contrib.gis.geos import Point
from rest_framework import filters


class PointFilter(filters.SearchFilter):

    search_title = 'Point'
    search_description = 'Search By Point'

    def filter_queryset(self, request, queryset, view):
        str_point = request.query_params.get('search_by', '')

        if str_point:
            lat, lng = str_point.split(',')
            queryset = queryset.filter(region__contains=Point(float(lat), float(lng)))
        return queryset

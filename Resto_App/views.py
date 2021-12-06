from django.db.models import query
from django.shortcuts import render
from django.db.models.query import QuerySet
from Resto_App.models import Restaurant, district
from .models import Dish, sector
from . import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

#DishModelView 
class DishModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Dish.objects.all()
    serializer_class = serializers.dishserializer

#RestoModelView
class RestoModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Restaurant.objects.all()
    serializer_class = serializers.restaurantserializer

#DistrictModelView
class DistrictModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = district.objects.all()
    serializer_class = serializers.districtserializer

#SectorModelView 
class SectorModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = sector.objects.all()
    serializer_class = serializers.sectorserializer






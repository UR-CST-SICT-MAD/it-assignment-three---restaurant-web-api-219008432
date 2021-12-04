from django.db.models import fields
from django.db.models.query import QuerySet
from rest_framework import serializers
from Resto_App.models import Restaurant, Dish
from Resto_App.models import district,sector
from django.contrib.auth.models import User

class dishserializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'
class restaurantserializer(serializers.ModelSerializer):
    dish = dishserializer(read_only=True, many=True)
    class Meta:
        model = Restaurant
        fields = '__all__'

class sectorserializer (serializers.ModelSerializer):
    restaurant = restaurantserializer(read_only=True, many=True)
    
    class Meta:
        model = sector
        fields = '__all__'
        Restaurant = serializers.SlugRelatedField(slug_field="Name", queryset=Restaurant.objects.all())
class districtserializer(serializers.ModelSerializer):
    restaurant = restaurantserializer(read_only=True, many=True)
    class Meta:
        model = district
        fields = '__all__'  
 
   
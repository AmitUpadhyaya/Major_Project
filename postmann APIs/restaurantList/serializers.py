from rest_framework import serializers
from .models import Restaurants


class RestaurantSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    cuisine = serializers.CharField(max_length=50)
    rating = serializers.IntegerField()
    image = serializers.ImageField()

    def create(self, validated_data):
        return Restaurants.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.name = validated_data.get('name', instance.name)
        instance.cuisine = validated_data.get('cuisine', instance.cuisine)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance
from .models import *
from rest_framework import serializers


class MerchPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchPhoto
        fields = ('id', 'image', 'uploaded_at')

class MerchSerializer(serializers.ModelSerializer):
    photos = MerchPhotoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Merch
        fields = ('id', 'name', 'description', 'price', 'stock', 'photos', 'created_at')


class MerchCreateSerializer(serializers.ModelSerializer):
    photos = serializers.ListField(
        child=serializers.ImageField(), write_only=True
    )

    class Meta:
        model = Merch
        fields = ['id', 'name', 'description', 'price', 'stock', 'photos']

    def create(self, validated_data):
        photos_data = validated_data.pop('photos')
        merch = Merch.objects.create(**validated_data)
        for photo_data in photos_data:
            MerchPhoto.objects.create(merch=merch, image=photo_data)
        return merch
    

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'email', 'phone', 'message', 'created_at')

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('id', 'email', 'created_at')
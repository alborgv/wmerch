from django.shortcuts import render

from rest_framework import generics

from .serializers import *
from .models import *
from .filters import *

class MerchView(generics.ListAPIView):
    queryset = Merch.objects.all()
    serializer_class = MerchSerializer
    filterset_class = MerchFilter

class createMerchView(generics.CreateAPIView):
    queryset = Merch.objects.all()
    serializer_class = MerchCreateSerializer

class updateMerchView(generics.UpdateAPIView):
    queryset = Merch.objects.all()
    serializer_class = MerchSerializer

class deleteMerchView(generics.DestroyAPIView):
    queryset = Merch.objects.all()
    serializer_class = MerchSerializer

class ContactView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class createContactView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class SubscriptionView(generics.ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    
class createSubscriptionView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
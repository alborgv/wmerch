from django.urls import path

from .views import *

urlpatterns = [
    path("merch/", MerchView.as_view() , name="merch"),
    path("merch/create/", createMerchView.as_view() , name="create_merch"),
    path("merch/update/<int:pk>", updateMerchView.as_view() , name="update_merch"),
    path("merch/delete/<int:pk>", deleteMerchView.as_view() , name="delete_merch"),
    path("contact/", ContactView.as_view() , name="contact"),
    path("contact/create/", createContactView.as_view() , name="create_contact"),
    path("subscription/", SubscriptionView.as_view() , name="subscription"),
    path("subscription/create/", createSubscriptionView.as_view() , name="create_subscription"),
]
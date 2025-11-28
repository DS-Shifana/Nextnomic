
from django.urls import path
from . import views

urlpatterns = [
    path("", views.ad_form, name="ad_form"),
    path("success/", views.success, name="success"),
]

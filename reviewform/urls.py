# reviewform/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_form, name='review_form'),
    path('success/', views.submitted, name='submitted'),
]

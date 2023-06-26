from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('campaigns/', views.campaign, name="campaign"),
    path('campaign-list/', views.wa_camps, name="list_camp"),
    path('journey/', views.automation, name="journey"),
]
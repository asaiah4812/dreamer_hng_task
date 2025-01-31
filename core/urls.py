from django.urls import path
from . import views

urlpatterns = [
    path('', views.DreamerList.as_view())
]

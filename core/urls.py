from django.urls import path
from . import views

urlpatterns = [
    path('', views.dreamer_list, name='dreamer_list'),
]

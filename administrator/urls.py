from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('findPharmacy/', views.findPharmacy, name='findPharmacy'),
]

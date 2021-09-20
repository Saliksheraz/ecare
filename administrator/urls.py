from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('findPharmacy/', views.findPharmacy, name='findPharmacy'),
]

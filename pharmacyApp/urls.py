"""pharmacyApp URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from administrator import rest_frame_work
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from pharmacyApp import settings
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register(r'pharmacies', rest_frame_work.pharmacyViewSet)
router.register(r'products', rest_frame_work.productsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productsViewSet2/', rest_frame_work.productsViewSet2),
    path('routers/', include(router.urls)),
    path('', include('administrator.urls')),
    path('diagnostics/', include('diagnostics.urls')),
    path('auth/', obtain_auth_token),

    path('accounts/', include('allauth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

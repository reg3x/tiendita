"""tiendita URL Configuration

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
from django.contrib import admin
from django.urls import path

from management.views import ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', ProductListView.as_view(), name='productos'),
    path('productos/crear', ProductCreateView.as_view(), name='crear-producto'),
    path('productos/<int:pk>', ProductDetailView.as_view(), name='detalle-producto'),
    path('productos/actualizar', ProductUpdateView.as_view(), name='crear-producto'),

]

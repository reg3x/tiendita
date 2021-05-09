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
from django.shortcuts import redirect

from management.views import ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView, BrandListView, \
    BrandCreateView, BrandDetailView, BrandUpdateView

urlpatterns = [
    path(r'^/$', ProductListView.as_view()),
    path('admin/', admin.site.urls),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/create', ProductCreateView.as_view(), name='create-product'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='detalle-product'),
    path('products/update', ProductUpdateView.as_view(), name='update-product'),
    path('brands/', BrandListView.as_view(), name='Brands'),
    path('brands/create', BrandCreateView.as_view(), name='create-brand'),
    path('brands/<int:pk>', BrandDetailView.as_view(), name='detalle-brand'),
    path('brands/update', BrandUpdateView.as_view(), name='update-brand'),

]

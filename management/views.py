from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from management.forms import ProductForm
from management.models import Product


class ProductView(object):

    model = Product
    form_class = ProductForm


class ProductListView(ProductView,
                      ListView):

    pass


class ProductCreateView(ProductView,
                        CreateView):

    pass


class ProductDetailView(ProductView,
                        DetailView):

    pass


class ProductUpdateView(ProductView,
                        UpdateView):

    pass

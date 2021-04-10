from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from management.forms import ProductForm, BrandForm
from management.models import Product, Brand


class ProductView(object):

    model = Product
    form_class = ProductForm


class ProductListView(ProductView,
                      ListView):

    pass


class ProductDetailView(ProductView,
                        DetailView):

    pass


class ProductCreateView(ProductView,
                        CreateView):

    success_url = ""


class ProductUpdateView(ProductView,
                        UpdateView):

    pass

#
#   Brand's Views
#


class BrandView(object):

    model = Brand
    form_class = BrandForm


class BrandListView(BrandView,
                    ListView):
    pass


class BrandDetailView(BrandView,
                      DetailView):

    pass


class BrandCreateView(BrandView,
                      CreateView):

    success_url = ""


class BrandUpdateView(BrandView,
                      UpdateView):

    pass

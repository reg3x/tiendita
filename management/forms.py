from django.forms import ModelForm

from management.models import Product, Brand


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = (
            "name",
            "cost",
            "sale_price",
            "brand",
            "categories",
        )


class BrandForm(ModelForm):

    class Meta:
        model = Brand
        fields = (
            "name",
        )

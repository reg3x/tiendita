from django.forms import ModelForm

from management.models import Product


class ProductForm(ModelForm):

    model = Product

    fields = (
        "name",
        "cost",
        "sale_price",
        "brand",
        "categories",
    )

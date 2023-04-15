from django import forms
from betterforms.multiform import MultiModelForm
from .models import Product, ProductManager


# 商品情報登録フォーム
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "name",
            "detail",
            "price",
            "name",
        )


# 商品管理者登録フォーム
class ProductManagerForm(forms.ModelForm):
    class Meta:
        model = ProductManager
        fields = (
            "name",
            "email",
            "phone_number",
        )


# 商品情報登録＋商品管理者登録フォーム（1つにまとめるフォーム）
class ProductMultiForm(MultiModelForm):
    form_classes = {
        "product_form": ProductForm,
        "product_manager_form": ProductManagerForm,
    }

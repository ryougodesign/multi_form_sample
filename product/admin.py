from django.contrib import admin
from .models import Product, ProductManager


# 商品情報登録フォーム管理画面
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "detail",
        "price",
        "created_at",
    )


# 商品管理者登録フォーム管理画面
class ProductManagerAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "email",
        "phone_number",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductManager, ProductManagerAdmin)

from django.db import models
from django.utils.translation import gettext_lazy as _


# 商品情報登録モデル
class Product(models.Model):
    # 商品名
    name = models.CharField(verbose_name=_("商品名"), max_length=64)

    # 商品詳細
    detail = models.TextField(verbose_name=_("商品詳細"), max_length=1000)

    # 商品金額
    price = models.PositiveIntegerField(verbose_name=_("商品金額"))

    # 登録日時
    created_at = models.DateTimeField(verbose_name=_("登録日時"), auto_now_add=True)


# 商品管理者登録モデル
class ProductManager(models.Model):
    # 担当者名
    name = models.CharField(verbose_name=_("担当者名"), max_length=32)

    # メールアドレス
    email = models.EmailField(verbose_name=_("email address"), max_length=256)

    # 電話番号
    phone_number = models.CharField(verbose_name=_("電話番号"), max_length=32)

from django.urls import path

from . import views

urlpatterns = [
    # トップページ
    path("", views.TopPage.as_view(), name="top"),
    # 商品登録ページ
    path("product/register/", views.ProductRegisterPage.as_view(), name="register"),
    # 商品登録完了ページ
    path("product/success/", views.ProductSuccessPage.as_view(), name="success"),
]

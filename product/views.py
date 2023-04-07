from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView
from .models import Product, ProductManager
from .forms import ProductMultiForm

# トップページ
class TopPage(TemplateView):
    template_name = "product/top.html"


# 商品登録ページ
class ProductRegisterPage(CreateView):
    template_name = "product/register.html"
    form_class = ProductMultiForm
    success_url = reverse_lazy("success")


# 商品登録ページ（データベース保存前に処理を追加したい場合）
# class ProductRegisterPage(CreateView):
#     template_name = "product/register.html"
#     form_class = ProductMultiForm
#     success_url = "success"

#     def form_valid(self, form):
#         product = form["product_form"].save(commit=False)
#         product_manager = form["product_manager_form"].save(commit=False)

#         # ここに処理をゴニョゴニョ書く

#         product.save()
#         product_manager.save()
#         return redirect(self.success_url)


# 商品登録成功ページ
class ProductSuccessPage(TemplateView):
    template_name = "product/success.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["products"] = Product.objects.all()
        ctx["product_managers"] = ProductManager.objects.all()
        return ctx

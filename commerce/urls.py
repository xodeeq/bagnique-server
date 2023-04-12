from django.urls import path

from commerce.views import GetCategoryProductsView, GetProductDetailView, GetProductsView, PostOrderView


app_name = "commerce"

urlpatterns = [
    path('products', GetProductsView.as_view(), name='products'),
    path('product-category/<int:category_id>/', GetCategoryProductsView.as_view(), name='product-category'),
    path('product/<int:id>/', GetProductDetailView.as_view(), name='product'),
    path('place-order', PostOrderView.as_view(), name='place-order'),
]
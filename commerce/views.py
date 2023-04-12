from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView

from commerce.models import Order, Product
from commerce.serializers import OrderSerializer, ProductSerializer

# Create your views here.


class GetProductsView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ["categories__title", "title", "description", 
                     "parent_product__title", "parent_product__description", 
                     "parent_product__categories__title"]
    


class GetCategoryProductsView(ListAPIView):
    serializer_class = ProductSerializer
    search_fields = ["categories__title", "title", "description", 
                     "parent_product__title", "parent_product__description", 
                     "parent_product__categories__title"]
    
    def get_queryset(self):
        return Product.objects.filter(
            categories__id__contains=self.kwargs["category_id"])


class PostOrderView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class GetProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"
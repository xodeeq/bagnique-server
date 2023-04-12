from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField


from commerce.models import Category, Order, OrderProduct, Product, ProductImage


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    product_images = ProductImageSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'available_quantity',
                   'out_of_stock', 'product_images' ]


class CategorySerializer(ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'title']



class OrderProductSerializer(ModelSerializer):
    product = PrimaryKeyRelatedField(read_only=False, queryset=Product.objects.all())

    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity']


class OrderSerializer(ModelSerializer):
    order_products = OrderProductSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = ['name', 'email', 'phone', 'city', 'state', 'zip_code', 'address', 'order_products']

    def create(self, validated_data):
        order_products = validated_data.pop('order_products', [])
        order = Order.objects.create(**validated_data)
        # OrderProduct.objects.bulk_create(order=order, **order_products)
        for order_product in order_products:
            OrderProduct.objects.create(order=order, **order_product)
            # If slow, consider using .bulk_create()
        return order
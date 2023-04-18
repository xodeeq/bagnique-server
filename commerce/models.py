from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

# Create your models here.




# class CloudinaryField(BaseCloudinaryField):
#     def upload_options(self, model_instance):
#         return {
#             'public_id': model_instance.__str__,
#             'folder': 'bagnique/product-images/',
#             'unique_filename': False,
#             'overwrite': True,
#             'resource_type': 'image',
#             'tags': ['product', 'bag'],
#             'invalidate': True,
#             'quality': 'auto:eco',
#         }



class Category(models.Model):
    title = models.CharField(max_length=18)
    is_main = models.BooleanField(default=False, help_text="To be displayed in the hero section")
    is_top = models.BooleanField(default=False, help_text="To be displayed on website header")

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    categories = models.ManyToManyField(Category, related_name='products')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available_quantity = models.PositiveSmallIntegerField()
    parent_product = models.ForeignKey("self", on_delete=models.SET_NULL, related_name="variations", blank=True, null=True)
    

    def __str__(self):
        return self.title
    
    def out_of_stock(self):
        return self.available_quantity < 1


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    file = CloudinaryField('image')

    def __str__(self):
        return '{} img-{}'.format(str(self.product), str(self.id))
    
    def get_image_url(self):
        print(self.file)
        return'{}{}'.format(settings.CLOUDINARY_ROOT_URL, self.file)


class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.product) + " (" + str(self.quantity) + ")"
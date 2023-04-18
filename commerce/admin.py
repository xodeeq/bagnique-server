from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from commerce.models import Category, Order, OrderProduct, Product, ProductImage

# Register your models here.

User = get_user_model()


class CategoryAdmin(admin.ModelAdmin):
    pass


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    classes = ("collapse",)
    extra = 0
    max_num = 4


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    pass


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    classes = ("collapse",)
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductInline]
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
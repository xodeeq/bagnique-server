from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from cms.models import Category, Product, ProductImage

# Register your models here.

User = get_user_model()

class CategoryAdmin(admin.ModelAdmin):
    pass


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    classes = ("collapse",)


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
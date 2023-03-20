from django.contrib import admin
from cms.models import Category, Product, ProductImage

# Register your models here.

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

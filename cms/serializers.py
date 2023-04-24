from rest_framework.serializers import ModelSerializer, SerializerMethodField
from cms.models import HeroContent, SiteContent

from commerce.models import Category, Product
from commerce.serializers import CategorySerializer, ProductSerializer


class HeroContentSerializer(ModelSerializer):
    top_products = SerializerMethodField('get_top_products')
    top_category = SerializerMethodField('get_top_category')

    class Meta:
        model = SiteContent
        fields = ['hero_primary_text', 'hero_secondary_text',
                  'hero_paragraph', 'top_products', 'top_category']
        read_only_fields = ['hero_primary_text',
                            'hero_secondary_text', 'hero_paragraph', 'top_products', 'top_category']

    def get_top_products(self, obj):
        try:
            return ProductSerializer(Product.objects.filter(categories__is_main=True).distinct()[:4], many=True).data
        except Product.DoesNotExist:
            return ProductSerializer(Product.objects.none(), many=True).data

    def get_top_category(self, obj):
        try:
            return CategorySerializer(Category.objects.filter(is_main=True).last()).data
        except Category.DoesNotExist:
            return CategorySerializer(Category.objects.none()).data


class BusinessInfoSerializer(ModelSerializer):

    class Meta:
        model = SiteContent
        fields = ['email_address', 'phone', 'address']
        read_only_fields = ['email_address', 'phone', 'address']


class SocialInfoSerializer(ModelSerializer):

    class Meta:
        model = SiteContent
        fields = ['whatsapp', 'telegram', 'instagram', 'facebook']
        read_only_fields = ['whatsapp', 'telegram', 'instagram', 'facebook']


class AboutUsSerializer(ModelSerializer):

    class Meta:
        model = SiteContent
        fields = ['short_about_us', 'long_about_us', 'buniess_image']
        read_only_fields = ['short_about_us', 'long_about_us', 'buniess_image']

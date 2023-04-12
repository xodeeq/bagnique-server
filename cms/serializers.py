from rest_framework.serializers import ModelSerializer, SerializerMethodField
from cms.models import HeroContent, SiteContent

from commerce.models import Product
from commerce.serializers import ProductSerializer


class HeroContentSerializer(ModelSerializer):
    top_products = SerializerMethodField('get_top_products')

    class Meta:
        model = SiteContent
        fields = ['hero_primary_text', 'hero_secondary_text', 'hero_paragraph', 'top_products']
        read_only_fields = ['hero_primary_text', 'hero_secondary_text', 'hero_paragraph', 'top_products']

    def get_top_products(self, obj):
        try:
            return ProductSerializer(Product.objects.filter(categories__is_top=True).distinct()[:4], many=True).data
        except Product.DoesNotExist:
            return ProductSerializer(Product.objects.none(), many=True).data


class ContactDetailSerializer(ModelSerializer):

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
        fields = ['short_about_us', 'long_about_us']
        read_only_fields = ['short_about_us', 'long_about_us']

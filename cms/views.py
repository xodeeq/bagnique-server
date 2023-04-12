from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from cms.models import HeroContent, SiteContent

from cms.serializers import AboutUsSerializer, ContactDetailSerializer, HeroContentSerializer, SocialInfoSerializer
from commerce.models import Category
from commerce.serializers import CategorySerializer

# Create your views here.


class GetHeroContentView(RetrieveAPIView):
    queryset = SiteContent.objects.all()
    serializer_class = HeroContentSerializer

    def get_object(self):
        return SiteContent.objects.filter(is_active=True).first()
    


class GetContactDetailView(RetrieveAPIView):
    queryset = SiteContent.objects.all()
    serializer_class = ContactDetailSerializer

    def get_object(self):
        return SiteContent.objects.filter(is_active=True).first()
    


class GetSocialInfoView(RetrieveAPIView):
    queryset = SiteContent.objects.all()
    serializer_class = SocialInfoSerializer

    def get_object(self):
        return SiteContent.objects.filter(is_active=True).first()
    

class GetAboutUsView(RetrieveAPIView):
    queryset = SiteContent.objects.all()
    serializer_class = AboutUsSerializer

    def get_object(self):
        return SiteContent.objects.filter(is_active=True).first()


class GetTopCategories(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        try:
            return Category.objects.filter(is_top=True)[:5]
        except Category.DoesNotExist:
            return Category.objects.none()
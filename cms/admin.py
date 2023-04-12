from django.contrib import admin
from django.contrib.auth import get_user_model

from cms.models import AboutUs, ContactDetail, HeroContent, SiteContent, SocialDetail

# Register your models here.

User = get_user_model()

admin.site.register(SiteContent)

admin.site.register(HeroContent)

admin.site.register(ContactDetail)

admin.site.register(SocialDetail)

admin.site.register(AboutUs)
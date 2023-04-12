from django.db import models

# Create your models here.


class SiteContent(models.Model):
    """Contents for the client hero section"""
    hero_primary_text = models.CharField(max_length=200)
    hero_secondary_text = models.CharField(max_length=200)
    hero_paragraph = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    """Contact details to be displayed on the client side"""
    email_address = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    """Social media information as contact back-up"""
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    telegram = models.CharField(max_length=20, blank=True, null=True)
    instagram = models.CharField(max_length=20, blank=True, null=True)
    facebook = models.CharField(max_length=20, blank=True, null=True)

    """Details for client-side about us section"""
    short_about_us = models.CharField(max_length=200, blank=True, null=True)
    long_about_us = models.TextField()

    def __str__(self):
        if self.is_active:
            return "Active Hero Content";
        else:
            return "In-active Hero Content"


class HeroContent(models.Model):
    """Contents for the client hero section"""
    hero_primary_text = models.CharField(max_length=200)
    hero_secondary_text = models.CharField(max_length=200)
    hero_paragraph = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        if self.is_active:
            return "Active Hero Content";
        else:
            return "In-active Hero Content"


class ContactDetail(models.Model):
    """Contact details to be displayed on the client side"""
    email_address = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()


class SocialDetail(models.Model):
    """Social media information as contact back-up"""
    whatsapp = models.CharField(max_length=20)
    telegram = models.CharField(max_length=20)
    instagram = models.CharField(max_length=20)
    facebook = models.CharField(max_length=20)


class AboutUs(models.Model):
    """Details for client-side about us section"""
    short_description = models.CharField(max_length=200)
    long_description = models.TextField()
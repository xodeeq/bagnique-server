from django.urls import path

from cms.views import GetAboutUsView, GetContactDetailView, GetHeroContentView, GetSocialInfoView, GetTopCategories


app_name = "cms"

urlpatterns = [
    path('hero-content', GetHeroContentView.as_view(), name='hero-content'),
    path('top-categories', GetTopCategories.as_view(), name='top-categories'),
    path('contact-detail', GetContactDetailView.as_view(), name='contact-detail'),
    path('socials', GetSocialInfoView.as_view(), name='socials'),
    path('about-us', GetAboutUsView.as_view(), name='about-us'),
]
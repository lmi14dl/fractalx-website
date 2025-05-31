from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('support/', views.support, name='support'),
    path('contact/', views.contact, name='contact'),
    path('privacy/', views.privacy, name="privacy"),
    path('terms/', views.terms, name="terms"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.urls import path
from .views import HomePageView, AboutPageView, RAMPageView, CpuPageView, PsuPageView, GpuPageView,MboardPageView


urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'), # new
    path('', HomePageView.as_view(), name='home'),
    path('RAM/', RAMPageView.as_view(), name='ram'),
    path('CPU/', CpuPageView.as_view(), name='cpu'),
    path('PSU/', PsuPageView.as_view(), name='psu'),
    path('GPU/', GpuPageView.as_view(), name='gpu'),
    path('MBOARD/', MboardPageView.as_view(), name='mboard'),
]

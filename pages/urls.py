from django.urls import path
from .views import HomePageView, AboutPageView, RAMPageView, CpuPageView, PsuPageView, GpuPageView,MboardPageView,StoragePageView


urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'), # new
    path('', HomePageView.as_view(), name='home'),
    path('ram/', RAMPageView.as_view(), name='ram'),
    path('cpu/', CpuPageView.as_view(), name='cpu'),
    path('psu/', PsuPageView.as_view(), name='psu'),
    path('gpu/', GpuPageView.as_view(), name='gpu'),
    path('motherboard/', MboardPageView.as_view(), name='mboard'),
    path('storage/', StoragePageView.as_view(), name='storage'),
]

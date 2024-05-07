from django.urls import path
from .views import ZiyoratgohHomeView, ZiyoratgohDetailView,HomePageView,ContactView,AboutUsView,ziyoratgoh_list_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('ziyoratgohlar/', ziyoratgoh_list_view, name='ziyoratgoh_list'),
    path('ziyoratgoh/<uuid:pk>/', ZiyoratgohDetailView.as_view(), name='ziyoratgoh_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutUsView.as_view(), name='about'),
]

from django.urls import path
from .views import CarParksListAPIView, CarParksDetailAPIView, CarParksUpdateAPIView, CarParksDeleteAPIView

urlpatterns = [
    path('list', CarParksListAPIView.as_view(), name='list'),
    path('detail/<pk>', CarParksDetailAPIView.as_view(), name='detail'),
    path('update/<pk>', CarParksUpdateAPIView.as_view(), name='update'),
    path('delete/<pk>', CarParksDeleteAPIView.as_view(), name='delete'),
]
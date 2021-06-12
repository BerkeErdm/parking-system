from django.urls import path
from .views import AccountListAPIView, AccountDetailAPIView, AccountUpdateAPIView, AccountDeleteAPIView

urlpatterns = [

path('list', AccountListAPIView.as_view(), name='list'),
path('detail/<pk>', AccountDetailAPIView.as_view(), name='detail'),
path('update/<pk>', AccountUpdateAPIView.as_view(), name='update'),
path('delete/<pk>', AccountDeleteAPIView.as_view(), name='delete'),
]
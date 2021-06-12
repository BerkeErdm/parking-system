from django.urls import path
from signin.api.views import (
                            UpdatePass,
                            ProfileView
                            )
app_name = "signin"
urlpatterns = [
path('me', ProfileView.as_view(), name='me'),
path('change-password', UpdatePass.as_view(), name='change-password'),

]
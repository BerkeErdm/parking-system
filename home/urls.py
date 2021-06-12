from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('account.urls')),
    path('api/carparks/', include('carparks.urls')),
    #path('api/profile/', include('signin.api.urls')),

    #Üye girişi urls'i
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    #SignIn API Oluşturma
    path('api/user/', include('signin.api.urls', namespace='signin')),

    #path('api/user/', include('signin.api.urls')),
]

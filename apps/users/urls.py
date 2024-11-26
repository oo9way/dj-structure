from apps.users import api_endpoints
from django.urls import path


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("login/", api_endpoints.NewLoginAPIView.as_view(), name="login-user"),
    path("login/by-telegram/", api_endpoints.LoginByTelegramConfirmAPIView.as_view(), name="login-telegram"),
    path("login/confirm/", api_endpoints.NewLoginConfirmAPIView.as_view(), name="confirm-login-user"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from gathering_server.users.views import SignUpView

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path('token/verify/', TokenVerifyView.as_view(), name="verify"),
]

urlpatterns += [
    path('signup/', SignUpView.as_view(), name="sign-up")
]

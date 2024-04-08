from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserListAPIView, UserUpdateApiView, UserCreateApiView, UserRetrieveApiView

app_name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', UserListAPIView.as_view(), name='user_list'),
    path('create/', UserCreateApiView.as_view(), name='user_create'),
    path('update/<int:pk>', UserUpdateApiView.as_view(), name='user_update'),
    path('detail/<int:pk>', UserRetrieveApiView.as_view(), name='user_detail'),
]
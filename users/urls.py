from django.urls import path

from users.apps import UsersConfig
from users.views import UserListAPIView, UserUpdateApiView, UserCreateApiView, UserRetrieveApiView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user_list'),
    path('create/', UserCreateApiView.as_view(), name='user_create'),
    path('update/<int:pk>', UserUpdateApiView.as_view(), name='user_update'),
    path('detail/<int:pk>', UserRetrieveApiView.as_view(), name='user_detail'),
]
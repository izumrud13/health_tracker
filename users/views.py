from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from habits.permissions import IsOwner
from users.models import User
from users.serializers import UserSerializers


# Create your views here.
class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserCreateApiView(generics.CreateAPIView):
    """Контроллер для создания пользователя"""
    serializer_class = UserSerializers
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = UserSerializers
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)

    def perform_create(sself, request, *args, **kwargs):
        data = request.data
        password = data.get('password')
        user = User.objects.get(email=data.get('email'))
        user.set_password(password)
        user.save()


class UserUpdateApiView(generics.UpdateAPIView):
    "Контролер для обновления данных пользователя"
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class UserRetrieveApiView(generics.RetrieveAPIView):
    "Контроллер для просмотра пользователя"
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

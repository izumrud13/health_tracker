from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.permissions import IsOwner
from habits.serializers import HabitSerializers


class HabitsListApiView(generics.ListAPIView):
    """Контролер для вывода списка привычек"""
    serializer_class = HabitSerializers
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        queryset = Habit.objects.filter(owner=user)
        return queryset


# Create your views here.
class HabitsCreateAPIView(generics.CreateAPIView):
    "Контролер для создания привычек"
    serializer_class = HabitSerializers
    permission_classes = [IsAuthenticated]


class HabitsRetrieveApiView(generics.RetrieveAPIView):
    "Контролер для вывода привычек"
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsUpdateApiView(generics.UpdateAPIView):
    "Контролер для обновления привычек"
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsDestroyApiView(generics.DestroyAPIView):
    "Контролер удаления привычек"
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PublicHabitsListApiView(generics.DestroyAPIView):
    "Контролер для вывода списка публичных привычек"
    serializer_class = HabitSerializers
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = [IsAuthenticated, IsOwner]

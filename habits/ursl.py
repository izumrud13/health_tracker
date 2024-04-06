from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitsListApiView, HabitsCreateAPIView, HabitsRetrieveApiView, HabitsUpdateApiView, \
    HabitsDestroyApiView, PublicHabitsListApiView

app_name = HabitsConfig.name

urlpatterns = [
    path('habits/', HabitsListApiView.as_view(), name='habits_list'),
    path('habits/create/', HabitsCreateAPIView.as_view(), name='habits_create'),
    path('habits/<int:pk>', HabitsRetrieveApiView.as_view(), name='habits_create'),
    path('habits/update/<int:pk>', HabitsUpdateApiView.as_view(), name='habits_create'),
    path('habits/delete/<int:pk>', HabitsDestroyApiView.as_view(), name='habits_create'),
    path('public_habits/', PublicHabitsListApiView.as_view(), name='habits_create'),
]
from django.conf import settings
from django.db import models

# Create your models here.
NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    place = models.CharField(max_length=100, verbose_name='Место')
    time = models.TimeField(default='10:30:00', verbose_name='Время')
    date = models.DateField(verbose_name='Дата', **NULLABLE)
    action = models.CharField(max_length=150, verbose_name='Действие')
    is_pleasant_habit = models.BooleanField(default=False, verbose_name="Признак приятной привычки")
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name="Связанная привычка", **NULLABLE)
    frequency = models.IntegerField(default=1, verbose_name='Переодичность', **NULLABLE)
    reward = models.CharField(max_length=300, verbose_name='Вознаграждение', **NULLABLE)
    lead_time = models.PositiveIntegerField(verbose_name='Время на выполнение', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def __str__(self):
        return f'{self.owner} будет {self.action} в {self.time} в {self.place}.'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

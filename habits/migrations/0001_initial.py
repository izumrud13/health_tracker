# Generated by Django 5.0.4 on 2024-04-06 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, verbose_name='Место')),
                ('time', models.TimeField(default='10:30:00', verbose_name='Время')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата')),
                ('action', models.CharField(max_length=150, verbose_name='Действие')),
                ('is_pleasant_habit', models.BooleanField(default=False, verbose_name='Признак приятной привычки')),
                ('frequency', models.IntegerField(blank=True, default=1, null=True, verbose_name='Переодичность')),
                ('reward', models.CharField(blank=True, max_length=300, null=True, verbose_name='Вознаграждение')),
                ('lead_time', models.PositiveIntegerField(blank=True, null=True, verbose_name='Время на выполнение')),
                ('is_public', models.BooleanField(default=False, verbose_name='Признак публичности')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]

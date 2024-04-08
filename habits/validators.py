from rest_framework.serializers import ValidationError


class RelateAndRewardValidator:

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        reward = dict(value).get(self.field2)

        if related_habit and reward:
            raise ValidationError('Запрещен одновременный выбор связанной привычки и указания вознаграждения')


class HabitTimeDurationValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        duration = dict(value).get(self.field)

        if duration and duration > 120:
            raise ValidationError('Время выполнения должно быть не больше 120 секунд')


class HabitRelatedHabitIsPleasantValidator:

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        is_pleasant = dict(value).get(self.field2)

        if related_habit and not is_pleasant:
            raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки')


class HabitPleasantValidator:

    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        reward = dict(value).get(self.field2)
        is_pleasant = dict(value).get(self.field3)

        if is_pleasant and reward and related_habit:
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')


class CheckHabitValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        frequency = dict(value).get(self.field)

        if isinstance(frequency, int) and (frequency > 7 or frequency < 1):
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')

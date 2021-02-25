from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from account.models import User
from django.utils import timezone


class Section(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, related_name="user_section")
    title = models.CharField("Название", max_length=130)

    class Meta:
        verbose_name_plural = "Cекции"
        verbose_name = "Секция"

    def __str__(self):
        return self.title


class Workout(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, related_name="user_workout")
    section = models.ForeignKey(User, verbose_name="Секция", on_delete=models.CASCADE, related_name="section")
    start_time = models.TimeField("Время начала тренировки")
    end_time = models.TimeField("Время окончания тренировки")
    date = models.DateField("Дата тренировки", default=timezone.now)

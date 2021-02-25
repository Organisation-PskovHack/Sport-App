from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from account.models import User
from django.utils import timezone


class Section(models.Model):
    user = models.ForeignKey(User, verbose_name="Преподаватель", on_delete=models.CASCADE, related_name="user")
    title = models.CharField("Название секции", max_length=130)
    slug = models.SlugField("URL секции", max_length=200)
    description = RichTextUploadingField('Информая о секции', blank=True)

    class Meta:
        verbose_name_plural = "Cекции"
        verbose_name = "Секция"

    def __str__(self):
        return self.title


class Workout(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, related_name="user_workout")
    section = models.ForeignKey(Section, verbose_name="Секция", on_delete=models.CASCADE,
                                related_name="section_workout")
    start_time = models.TimeField("Время начала тренировки", blank=True)
    end_time = models.TimeField("Время окончания тренировки", blank=True)
    date = models.DateField("Дата тренировки", default=timezone.now)

    class Meta:
        verbose_name_plural = "Тренировки"
        verbose_name = "Тренировка"


class UserSection(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, related_name="user_section")
    section = models.ForeignKey(Section, verbose_name="Секция", on_delete=models.CASCADE, related_name="section")

    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"

    def __str__(self):
        return User.objects.get(id=self.user_id).first_name

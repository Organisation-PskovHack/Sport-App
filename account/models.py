from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class User(AbstractUser, UserManager):
    group = models.CharField("Группа", max_length=130, blank=True)
    description = RichTextUploadingField('Информая о пользователе', blank=True)
    patronymic = models.CharField("Отчество", max_length=130, blank=True)
    is_student = models.BooleanField("Это студент?", default=True, blank=False,
                                     help_text="Убрать, если это преподаватель.")
    qr_path = models.CharField("Путь к QR коду", blank=True, max_length=210)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.first_name

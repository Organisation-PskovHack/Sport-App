from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class User(AbstractUser, UserManager):
    group = models.CharField("Группа", max_length=130)
    description = RichTextUploadingField('Информая о пользователе', blank=True)
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.first_name

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class User(AbstractUser, UserManager):
    group = models.CharField("Группа", max_length=130, blank=True)
    description = RichTextUploadingField('Информая о пользователе', blank=True)
    patronymic = models.CharField("Отчество", max_length=130, blank=True)
    is_student = models.BooleanField("Это студент?", default=True, blank=False,
                                     help_text="Убрать, если это преподаватель.")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.first_name

    def get_full_name(self):
        full_name = '%s %s %s' % (self.last_name, self.first_name, self.patronymic)
        return full_name.strip()

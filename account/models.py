from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _


class User(AbstractUser, UserManager):
    role_choices = ((_("Администратор"), _("Администатор")),
                    (_("Преподаватель"), _("Преподаватель")),
                    (_("Студент"), _("Студент")),)
    middle_name = models.CharField("Отчество", max_length=50, default='', blank=True)
    faculty = models.CharField("Факультет", max_length=255, default='')
    group_number = models.CharField("Номер группы", max_length=20, default="")
    role = models.CharField("Роль пользователя", max_length=50, default=_("Студент"), choices=role_choices)
    image = models.ImageField("Фотография пользователя", upload_to="user/image", default='user/image/no-image.png')
    qr_path = models.TextField("Путь к QR-коду", default="")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.first_name

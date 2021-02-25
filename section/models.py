from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from account.models import User


class Section(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, related_name="section")
    title = models.CharField("Название", max_length=130)

    class Meta:
        verbose_name_plural = "Cекции"
        verbose_name = "Секция"

    def __str__(self):
        return self.title

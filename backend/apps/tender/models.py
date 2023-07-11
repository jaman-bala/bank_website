from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Tender(models.Model):
    title = models.CharField("Название проекта", max_length=250)
    title_contracts = models.CharField("Название контракта", max_length=250)
    pricath = models.CharField("Номер приказа", max_length=250)
    text = RichTextUploadingField("Текст")
    file = models.FileField(upload_to='files', null=True, blank=True, verbose_name="Добавить файл")
    date = models.DateTimeField('Срок подачи заявок')
    is_active = models.BooleanField("Активный", default=True)
    created = models.DateTimeField(verbose_name="Дата создание", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    def save(self, *args, **kwargs):
        if self.file:
            # Выполняете действие с файлом
            file_value = self.file.url
        else:
            # Выполняете действие по умолчанию
            file_value = ''

        super(Tender, self).save(*args, **kwargs)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Тендер'
        verbose_name_plural = 'Тендера'
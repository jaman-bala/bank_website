# Generated by Django 4.1.3 on 2023-02-02 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Название'),
        ),
    ]

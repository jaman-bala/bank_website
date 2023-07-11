# Generated by Django 4.1.3 on 2023-05-17 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_gallery_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('url', models.URLField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Добавить видео',
            },
        ),
    ]
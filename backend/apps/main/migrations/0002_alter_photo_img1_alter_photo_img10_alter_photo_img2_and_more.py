# Generated by Django 4.1.3 on 2023-02-14 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='img1',
            field=models.ImageField(blank=True, upload_to='img', verbose_name='Фотография №1'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='img10',
            field=models.ImageField(blank=True, upload_to='img', verbose_name='Фотография №10'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='img2',
            field=models.ImageField(blank=True, upload_to='img', verbose_name='Фотография №2'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='img3',
            field=models.ImageField(blank=True, upload_to='img', verbose_name='Фотография №3'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='img4',
            field=models.ImageField(blank=True, upload_to='img', verbose_name='Фотография №4'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='img5',
            field=models.ImageField(blank=True, upload_to='img', verbose_name='Фотография №5'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='img6',
            field=models.ImageField(blank=True, upload_to='img', verbose_name='Фотография №6'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='img7',
            field=models.ImageField(blank=True, upload_to='img', verbose_name='Фотография №7'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='img8',
            field=models.ImageField(blank=True, upload_to='img', verbose_name='Фотография №8'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='img9',
            field=models.ImageField(blank=True, upload_to='img', verbose_name='Фотография №9'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=10, verbose_name='Название Каруселя'),
        ),
    ]

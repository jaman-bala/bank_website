# Generated by Django 4.1.3 on 2023-05-13 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_photo_img1_alter_photo_img10_alter_photo_img2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='img10',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='img3',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='img4',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='img5',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='img6',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='img7',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='img8',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='img9',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='text1',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='text10',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='text2',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='text3',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='text4',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='text5',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='text6',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='text7',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='text8',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='text9',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='title1',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='title10',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='title2',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='title3',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='title4',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='title5',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='title6',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='title7',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='title8',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='title9',
        ),
        migrations.AlterField(
            model_name='photo',
            name='img1',
            field=models.ImageField(blank=True, upload_to='img', verbose_name='Фотография'),
        ),
    ]

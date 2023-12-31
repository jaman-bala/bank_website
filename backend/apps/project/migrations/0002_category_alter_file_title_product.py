# Generated by Django 4.1.3 on 2023-05-17 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название категории')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Категория проекта',
                'verbose_name_plural': 'Категории категория',
            },
        ),
        migrations.AlterField(
            model_name='file',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название файла'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название проекта')),
                ('description', models.TextField(verbose_name='Описание')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.category')),
            ],
        ),
    ]

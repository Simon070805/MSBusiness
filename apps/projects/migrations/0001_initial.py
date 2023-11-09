# Generated by Django 4.2.6 on 2023-11-08 21:50

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название проекта')),
                ('descriptions', models.TextField(verbose_name='Описание проекта')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality='100', scale=None, size=[1920, 1080], upload_to='service_image/', verbose_name='Фотография проекта')),
            ],
            options={
                'verbose_name': 'Наши проекты',
                'verbose_name_plural': 'Наши проекты',
            },
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-09 07:13

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_operationprocess_delete_faqs_remove_price_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='descriptions_2',
            field=models.TextField(default=1, verbose_name='Описание №2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='image_2',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality='100', scale=None, size=[1920, 1080], upload_to='about_image', verbose_name='Фотография №2'),
        ),
        migrations.AddField(
            model_name='about',
            name='title_2',
            field=models.CharField(default=1, max_length=255, verbose_name='Заголовок №2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='youtube',
            field=models.URLField(blank=True, null=True, verbose_name='YouTube - ссылка на видео'),
        ),
    ]

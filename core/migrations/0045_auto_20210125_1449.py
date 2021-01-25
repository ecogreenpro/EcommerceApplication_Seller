# Generated by Django 3.1.4 on 2021-01-25 08:49

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_settings'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='privacyPolicy',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='returnPolicy',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]

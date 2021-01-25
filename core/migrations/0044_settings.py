# Generated by Django 3.1.4 on 2021-01-25 07:12

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_auto_20210124_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteTitle', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=255)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('logo', models.ImageField(blank=True, upload_to='Photos')),
                ('favIcon', models.ImageField(blank=True, upload_to='Photos')),
                ('facebook', models.CharField(blank=True, max_length=50)),
                ('instagram', models.CharField(blank=True, max_length=50)),
                ('twitter', models.CharField(blank=True, max_length=50)),
                ('youtube', models.CharField(blank=True, max_length=50)),
                ('aboutus', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('contact', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('isActive', models.BooleanField(default=False, max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
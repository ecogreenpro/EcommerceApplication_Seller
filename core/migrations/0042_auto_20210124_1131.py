# Generated by Django 3.1.4 on 2021-01-24 05:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_products_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='longDescirption',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='shortDescription',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
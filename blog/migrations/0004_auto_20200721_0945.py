# Generated by Django 3.0.6 on 2020-07-21 04:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200708_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='chead0',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='chead1',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='chead2',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]

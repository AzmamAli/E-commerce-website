# Generated by Django 4.1.7 on 2023-04-10 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_rename_head_heading_category_catt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='catt',
        ),
        migrations.DeleteModel(
            name='heading',
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-10 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_category_catt'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='head',
            new_name='heading',
        ),
        migrations.AddField(
            model_name='category',
            name='catt',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.heading'),
            preserve_default=False,
        ),
    ]

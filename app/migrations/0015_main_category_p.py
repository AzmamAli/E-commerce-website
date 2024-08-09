# Generated by Django 4.1.7 on 2023-04-10 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_category_catt_delete_heading'),
    ]

    operations = [
        migrations.CreateModel(
            name='main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='p',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.main'),
            preserve_default=False,
        ),
    ]

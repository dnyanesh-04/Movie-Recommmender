# Generated by Django 5.0.7 on 2024-07-29 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='movie',
            name='selectable',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]

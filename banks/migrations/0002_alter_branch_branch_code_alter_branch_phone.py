# Generated by Django 5.0.6 on 2024-06-24 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='branch_code',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='phone',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

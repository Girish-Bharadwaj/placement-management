# Generated by Django 4.1.4 on 2023-01-14 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_usn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='usn',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

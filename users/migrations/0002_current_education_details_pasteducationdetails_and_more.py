# Generated by Django 4.1.4 on 2023-01-14 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Current_Education_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_sem_sgpa', models.FloatField()),
                ('second_sem_sgpa', models.FloatField()),
                ('third_sem_sgpa', models.FloatField()),
                ('fourth_sem_sgpa', models.FloatField()),
                ('fifth_sem_sgpa', models.FloatField()),
                ('sixth_sem_sgpa', models.FloatField()),
                ('seventh_sem_sgpa', models.FloatField()),
                ('eighth_sem_sgpa', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PastEducationDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenth_scheme', models.CharField(max_length=100)),
                ('twelve_scheme', models.CharField(max_length=100)),
                ('cet_rank', models.CharField(max_length=100)),
                ('tenth_percentage', models.FloatField()),
                ('twelve_percentage', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='current_edu_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.current_education_details'),
        ),
        migrations.AddField(
            model_name='profile',
            name='past_edu_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.pasteducationdetails'),
        ),
    ]

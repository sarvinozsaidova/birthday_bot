# Generated by Django 5.0.3 on 2024-03-04 15:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('picture', models.ImageField(null=True, upload_to='')),
                ('date_of_birth', models.DateField()),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reminder.position')),
            ],
        ),
    ]
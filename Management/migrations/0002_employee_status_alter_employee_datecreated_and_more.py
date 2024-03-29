# Generated by Django 4.2.1 on 2023-05-20 10:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='status',
            field=models.CharField(default='Single', max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='dateCreated',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateField(),
        ),
    ]

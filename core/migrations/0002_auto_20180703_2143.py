# Generated by Django 2.0.7 on 2018-07-03 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callrecord',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]

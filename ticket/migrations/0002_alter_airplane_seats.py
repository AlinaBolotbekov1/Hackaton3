# Generated by Django 4.2.4 on 2023-08-31 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airplane',
            name='seats',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]

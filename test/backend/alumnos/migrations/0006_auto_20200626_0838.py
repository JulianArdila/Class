# Generated by Django 2.1 on 2020-06-26 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0005_auto_20200626_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='estado',
            field=models.BooleanField(default=1),
        ),
    ]

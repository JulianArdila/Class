# Generated by Django 3.0.3 on 2020-07-16 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0008_alumno_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

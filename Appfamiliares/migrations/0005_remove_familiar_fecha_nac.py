# Generated by Django 4.0.5 on 2022-07-07 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appfamiliares', '0004_familiar_fecha_nac'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familiar',
            name='fecha_nac',
        ),
    ]

# Generated by Django 4.0.5 on 2022-07-05 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appfamiliares', '0002_rename_familiares_familiar'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='apellido',
            field=models.CharField(default='Perez', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='familiar',
            name='edad',
            field=models.IntegerField(default='30'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='familiar',
            name='nombre',
            field=models.CharField(default='Carlos', max_length=30),
            preserve_default=False,
        ),
    ]

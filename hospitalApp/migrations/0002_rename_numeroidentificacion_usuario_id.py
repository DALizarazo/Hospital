# Generated by Django 4.1.1 on 2022-09-14 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='numeroIdentificacion',
            new_name='id',
        ),
    ]
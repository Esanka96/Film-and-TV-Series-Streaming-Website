# Generated by Django 4.2.6 on 2023-10-31 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_rename_register_registerform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registerform',
            old_name='Firstname',
            new_name='First_name',
        ),
        migrations.RenameField(
            model_name='registerform',
            old_name='Lastname',
            new_name='Last_name',
        ),
    ]

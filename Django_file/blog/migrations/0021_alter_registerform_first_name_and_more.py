# Generated by Django 4.2.6 on 2023-11-09 13:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_registerform_email_registerform_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerform',
            name='First_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='registerform',
            name='Last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='registerform',
            name='Password',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-09 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_tvtable_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmphoto',
            name='photo',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='posttable',
            name='photo',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=''),
        ),
    ]

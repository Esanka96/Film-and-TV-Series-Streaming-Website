# Generated by Django 4.2.6 on 2023-10-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_filmname_filmphoto_posttable_filmnames_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TVtable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-23 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_posttable_item_posttable_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posttable',
            name='item',
        ),
        migrations.AddField(
            model_name='posttable',
            name='item',
            field=models.ManyToManyField(to='blog.list'),
        ),
    ]

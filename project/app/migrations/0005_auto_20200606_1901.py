# Generated by Django 3.0.7 on 2020-06-06 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_merge_20200606_1901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply',
            old_name='img',
            new_name='reference',
        ),
        migrations.AlterField(
            model_name='post_editor',
            name='img',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post_youtuber',
            name='img',
            field=models.TextField(null=True),
        ),
    ]

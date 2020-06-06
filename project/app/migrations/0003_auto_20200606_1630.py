# Generated by Django 3.0.7 on 2020-06-06 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20200606_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_editor',
            name='basic_content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post_editor',
            name='basic_price',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post_editor',
            name='premium_content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post_editor',
            name='premium_price',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post_editor',
            name='standard_content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post_editor',
            name='standard_price',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post_editor',
            name='vid_url',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post_youtuber',
            name='price',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post_youtuber',
            name='vid_url',
            field=models.TextField(null=True),
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('datetime', models.DateTimeField()),
                ('img', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
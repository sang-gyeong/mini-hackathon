# Generated by Django 3.0.7 on 2020-06-06 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('rate', models.IntegerField()),
                ('datetime', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_e', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment_youtuber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('rate', models.IntegerField()),
                ('datetime', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_y', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post_editor',
            name='career',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post_editor',
            name='genre',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post_editor',
            name='period',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post_editor',
            name='rating',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post_editor',
            name='tool',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post_editor',
            name='work',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post_youtuber',
            name='career',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post_youtuber',
            name='genre',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post_youtuber',
            name='period',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post_youtuber',
            name='rating',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post_youtuber',
            name='tool',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post_youtuber',
            name='work',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post_editor',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post_editor',
            name='datetime',
            field=models.DateTimeField(null=True),
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
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='comment_youtuber',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_y', to='app.Post_youtuber'),
        ),
        migrations.AddField(
            model_name='comment_editor',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_e', to='app.Post_editor'),
        ),
    ]
# Generated by Django 4.0.2 on 2022-08-22 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insta_web', '0002_instagramdata_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramDownloaded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram_url', models.URLField(max_length=500)),
                ('instagram_pk', models.IntegerField(default=0)),
                ('instagram_id', models.CharField(max_length=30)),
                ('media_type', models.IntegerField()),
                ('instagram_user_pk', models.IntegerField(default=0)),
                ('instagram_username', models.CharField(max_length=300)),
                ('file', models.ImageField(blank=True, upload_to='instagram_downloaded/')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('searcher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

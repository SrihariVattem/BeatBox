# Generated by Django 5.1.3 on 2024-11-23 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover_image',
            field=models.ImageField(upload_to='media/album_covers/'),
        ),
    ]
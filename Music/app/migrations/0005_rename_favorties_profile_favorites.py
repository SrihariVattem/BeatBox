# Generated by Django 5.1.3 on 2024-11-24 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_favortie_profile_favorties'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='favorties',
            new_name='favorites',
        ),
    ]

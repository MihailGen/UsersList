# Generated by Django 5.1.4 on 2025-01-12 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]

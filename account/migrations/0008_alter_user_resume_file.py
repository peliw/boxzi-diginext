# Generated by Django 4.2 on 2024-06-01 14:13

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_user_resume_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='resume_file',
            field=models.FileField(blank=True, null=True, upload_to=account.models.user_directory_path, verbose_name='فایل pdf رزومه'),
        ),
    ]

# Generated by Django 4.2 on 2024-06-25 15:35

from django.db import migrations, models
import utils.uuid_generator


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0013_remove_startupteam_team_members_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='uuid',
            field=models.CharField(blank=True, default=utils.uuid_generator.random_uuid4, editable=False, max_length=36, unique=True),
        ),
        migrations.AlterField(
            model_name='roadregistration',
            name='uuid',
            field=models.CharField(blank=True, default=utils.uuid_generator.random_uuid4, editable=False, max_length=36, unique=True),
        ),
        migrations.AlterField(
            model_name='startupteam',
            name='uuid',
            field=models.CharField(blank=True, default=utils.uuid_generator.random_uuid4, editable=False, max_length=36, unique=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='uuid',
            field=models.CharField(blank=True, default=utils.uuid_generator.random_uuid4, editable=False, max_length=36, unique=True),
        ),
    ]

# Generated by Django 4.2 on 2024-05-30 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.uuid_generator


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, default=utils.uuid_generator.random_uuid, editable=False, max_length=5, unique=True)),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_update_time', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_of_topic', to=settings.AUTH_USER_MODEL, verbose_name='سازنده')),
            ],
            options={
                'verbose_name': 'موضوع',
                'verbose_name_plural': 'موضوعات',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, default=utils.uuid_generator.random_uuid, editable=False, max_length=5, unique=True)),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_update_time', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_of_subject', to=settings.AUTH_USER_MODEL, verbose_name='سازنده')),
                ('topic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topic_of_subject', to='subject.topic', verbose_name='موضوع')),
            ],
            options={
                'verbose_name': 'زیر موضوع',
                'verbose_name_plural': 'زیر موضوعات',
            },
        ),
    ]
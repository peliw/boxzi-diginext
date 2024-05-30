# Generated by Django 4.2 on 2024-05-30 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0002_initial'),
        ('account', '0001_initial'),
        ('subject', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_of_meeting', to='team.startupteam', verbose_name='تیم'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='team_member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_member_of_meeting', to=settings.AUTH_USER_MODEL, verbose_name='عضو تیم'),
        ),
        migrations.AddField(
            model_name='user',
            name='abilities',
            field=models.ManyToManyField(blank=True, related_name='abilities_of_user', to='subject.subject', verbose_name='توانایی ها'),
        ),
        migrations.AddField(
            model_name='user',
            name='access_to_center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.center', verbose_name='دسترسی به مرکز'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='interests',
            field=models.ManyToManyField(blank=True, related_name='interests_of_user', to='subject.subject', verbose_name='علاقه مندی ها'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
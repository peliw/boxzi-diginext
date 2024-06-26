# Generated by Django 4.2 on 2024-06-01 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0006_roadregistration_complete_registration_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='roadregistration',
            name='team_or_individual',
            field=models.CharField(choices=[('t', 'تیم'), ('i', 'فرد')], default='t', max_length=1, verbose_name='تیم یا فرد؟'),
        ),
        migrations.AlterField(
            model_name='roadregistration',
            name='status_user_state',
            field=models.CharField(choices=[('0', 'درحال تکمیل ثبت نام'), ('1', 'تکمیل ثبت نام اولیه'), ('f', 'ثبت نام کامل')], default='۱', max_length=2, verbose_name='وضعیت ثبت نام کاربر'),
        ),
    ]

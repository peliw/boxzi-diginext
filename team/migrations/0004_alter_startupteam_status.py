# Generated by Django 4.2 on 2024-05-31 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_alter_startupteam_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startupteam',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'فعال'), ('i', 'غیر فعال')], default='a', max_length=1, null=True, verbose_name='وضعیت'),
        ),
    ]
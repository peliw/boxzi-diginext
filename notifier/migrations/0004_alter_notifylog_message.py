# Generated by Django 4.2 on 2024-06-24 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifier', '0003_alter_notifylog_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifylog',
            name='message',
            field=models.TextField(null=True, verbose_name='پاسخ سرور'),
        ),
    ]
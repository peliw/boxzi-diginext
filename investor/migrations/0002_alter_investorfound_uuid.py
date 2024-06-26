# Generated by Django 4.2 on 2024-06-25 15:35

from django.db import migrations, models
import utils.uuid_generator


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investorfound',
            name='uuid',
            field=models.CharField(blank=True, default=utils.uuid_generator.random_uuid4, editable=False, max_length=36, unique=True),
        ),
    ]

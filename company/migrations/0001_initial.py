# Generated by Django 4.2 on 2024-05-30 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields
import utils.uuid_generator


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, default=utils.uuid_generator.random_uuid, editable=False, max_length=5, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name='اسم کسب و کار')),
                ('domain', models.URLField(max_length=255, verbose_name='دامنه')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='company/logo/', verbose_name='لوگو')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
                ('watching_subject', models.ManyToManyField(blank=True, related_name='watching_subject_of_company', to='subject.subject', verbose_name='موضوعات زیر نظر')),
            ],
            options={
                'verbose_name': 'کسب و کار',
                'verbose_name_plural': 'کسب و کار ها',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, default=utils.uuid_generator.random_uuid, editable=False, max_length=5, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name='نام خدمت یا محصول')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='مدال مورد نیاز')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_update_time', models.DateTimeField(auto_now=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_of_company', to='company.company', verbose_name='کمپانی')),
            ],
            options={
                'verbose_name': 'خدمت یا کالا',
                'verbose_name_plural': 'خدمت ها یا کالا ها',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, default=utils.uuid_generator.random_uuid, editable=False, max_length=5, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name='اسم مرکز')),
                ('short_description', models.TextField(default='', verbose_name='توضیحات کوتاه')),
                ('domain', models.URLField(blank=True, max_length=255, null=True, verbose_name='دامنه')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='company/logo/', verbose_name='لوگو')),
                ('state', models.CharField(max_length=255, verbose_name='استان')),
                ('type', models.CharField(choices=[('g', 'مرکز رشد'), ('a', 'مرکز شتابدهی'), ('i', 'کارخونه نوآوری')], max_length=1, verbose_name='نوع')),
                ('activity', models.CharField(max_length=255, verbose_name='حوزه فعالیت')),
                ('description', django_quill.fields.QuillField(blank=True, default='', verbose_name='توضیحات')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
                ('mentors', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='مربی ها')),
            ],
            options={
                'verbose_name': 'مرکز',
                'verbose_name_plural': 'مراکز',
            },
        ),
    ]

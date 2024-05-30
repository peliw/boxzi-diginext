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
        ('content', '0001_initial'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=128, verbose_name='متن')),
                ('is_valid', models.BooleanField(default=False, verbose_name='درست بودن')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان ساخت')),
                ('last_update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='زمان بروزرسانی')),
                ('accelerator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accelerator_of_answer', to='company.center', verbose_name='برگزارکننده')),
            ],
            options={
                'verbose_name': 'جواب',
                'verbose_name_plural': 'جواب ها',
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, default=utils.uuid_generator.random_uuid, editable=False, max_length=5, unique=True)),
                ('name', models.CharField(max_length=64, verbose_name='عنوان')),
                ('medals', models.PositiveIntegerField(default=0, verbose_name='مدال')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان ساخت')),
                ('last_update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='زمان بروزرسانی')),
                ('accelerator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accelerator_of_exam', to='company.center', verbose_name='برگزارکننده')),
            ],
            options={
                'verbose_name': 'آزمون',
                'verbose_name_plural': 'آزمون ها',
            },
        ),
        migrations.CreateModel(
            name='PreRegisterTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, default=utils.uuid_generator.random_uuid, editable=False, max_length=5, unique=True)),
                ('title', models.CharField(max_length=64, verbose_name='عنوان')),
                ('text', django_quill.fields.QuillField(default='', verbose_name='محتوا متنی')),
                ('start_date', models.DateField(null=True, verbose_name='تاریخ شروع')),
                ('expiration_date', models.DateField(null=True, verbose_name='تاریخ پایان')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان ساخت')),
                ('last_update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='زمان بروزرسانی')),
                ('accelerator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accelerator_of_pre_register_task', to='company.center', verbose_name='برگزارکننده')),
            ],
            options={
                'verbose_name': 'آزمون پیش ثبت نام',
                'verbose_name_plural': 'آزمون های پیش ثبت نام',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256, verbose_name='متن')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان ساخت')),
                ('last_update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='زمان بروزرسانی')),
                ('accelerator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accelerator_of_question', to='company.center', verbose_name='برگزارکننده')),
                ('answers', models.ManyToManyField(blank=True, to='quiz.answer', verbose_name='گزینه ها')),
            ],
            options={
                'verbose_name': 'سوآل',
                'verbose_name_plural': 'سوآل ها',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, default=utils.uuid_generator.random_uuid, editable=False, max_length=5, unique=True)),
                ('title', models.CharField(max_length=64, verbose_name='عنوان')),
                ('text', django_quill.fields.QuillField(default='', verbose_name='محتوا متنی')),
                ('medals', models.PositiveIntegerField(default=0, verbose_name='مدال')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان ساخت')),
                ('last_update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='زمان بروزرسانی')),
                ('accelerator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accelerator_of_task', to='company.center', verbose_name='برگزارکننده')),
            ],
            options={
                'verbose_name': 'تسک',
                'verbose_name_plural': 'تسک ها',
            },
        ),
        migrations.CreateModel(
            name='UserExamAnsewrHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان ساخت')),
                ('last_update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='زمان بروزرسانی')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ansewr_history_of_answer', to='quiz.answer')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ansewr_history_of_exam', to='quiz.exam')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ansewr_history_of_question', to='quiz.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ansewr_history_of_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'پاسخ ها کاربر',
                'verbose_name_plural': 'پاسخ های کاربر ',
            },
        ),
        migrations.CreateModel(
            name='TaskResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, default=utils.uuid_generator.random_uuid, editable=False, max_length=5, unique=True)),
                ('file', models.FileField(upload_to='task-response/%Y/%m/', verbose_name='فایل')),
                ('title', models.CharField(max_length=64, verbose_name='عنوان')),
                ('text', django_quill.fields.QuillField(default='', verbose_name='محتوا متنی')),
                ('status', models.CharField(choices=[('w', 'در انتظار برسی'), ('d', 'تایید شده'), ('r', 'رد شده')], default='w', max_length=1, verbose_name='وضعیت')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان ساخت')),
                ('last_update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='زمان بروزرسانی')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_of_task_response', to='quiz.task', verbose_name='تسک')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_of_task_response', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'پاسخ تسک',
                'verbose_name_plural': 'پاسخ تسک ها',
            },
        ),
        migrations.CreateModel(
            name='TaskOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, default=utils.uuid_generator.random_uuid, editable=False, max_length=5, unique=True)),
                ('row_number', models.PositiveIntegerField(verbose_name='شماره ردیف')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان ساخت')),
                ('last_update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='زمان بروزرسانی')),
                ('collection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collection_of_task_order', to='content.collection', verbose_name='فصل')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='road_of_task_order', to='quiz.task', verbose_name='تسک')),
            ],
            options={
                'verbose_name': 'ترتیب تسک',
                'verbose_name_plural': 'ترتیب تسک ها',
            },
        ),
        migrations.CreateModel(
            name='PreRegisterTaskResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, default=utils.uuid_generator.random_uuid, editable=False, max_length=5, unique=True)),
                ('file', models.FileField(blank=True, help_text='در صورت نیاز میتوانید یک فایل نیز برای شتابدهنده ارسال کنید', null=True, upload_to='task-response/%Y/%m/', verbose_name='فایل')),
                ('title', models.CharField(max_length=64, verbose_name='عنوان پاسخ')),
                ('text', django_quill.fields.QuillField(default='', verbose_name='محتوا متنی')),
                ('status', models.CharField(choices=[('w', 'در انتظار برسی'), ('d', 'تایید شده'), ('r', 'رد شده')], default='w', max_length=1, verbose_name='وضعیت')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان ساخت')),
                ('last_update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='زمان بروزرسانی')),
                ('road', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='road_of_pre_register_task_response', to='content.road', verbose_name='مسیر')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_of_pre_register_task_response', to='quiz.preregistertask', verbose_name='تسک')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_of_pre_register_task_response', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'پاسخ کاربر به آزمون',
                'verbose_name_plural': 'پاسخ های کاربر به آزمون',
            },
        ),
        migrations.CreateModel(
            name='PersonalTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, default=utils.uuid_generator.random_uuid, editable=False, max_length=5, unique=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان ساخت')),
                ('last_update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='زمان بروزرسانی')),
                ('road', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='road_of_personal_test', to='content.road', verbose_name='مسیر')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_of_personal_test', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'آزمون شخصیت',
                'verbose_name_plural': 'آزمون های شخصیت',
            },
        ),
        migrations.CreateModel(
            name='ExamOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, default=utils.uuid_generator.random_uuid, editable=False, max_length=5, unique=True)),
                ('row_number', models.PositiveIntegerField(verbose_name='شماره ردیف')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان ساخت')),
                ('last_update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='زمان بروزرسانی')),
                ('collection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collection_of_exam_order', to='content.collection', verbose_name='فصل')),
                ('exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='road_of_exam_order', to='quiz.exam', verbose_name='آزمون')),
            ],
            options={
                'verbose_name': 'ترتیب آزمون',
                'verbose_name_plural': 'ترتیب آزمون ها',
            },
        ),
        migrations.AddField(
            model_name='exam',
            name='questions',
            field=models.ManyToManyField(blank=True, to='quiz.question', verbose_name='سوال ها'),
        ),
    ]
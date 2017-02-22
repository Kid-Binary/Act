# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-22 10:10
from __future__ import unicode_literals

import act.services.file_name
import act.validators
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import metadata.mixins
import website.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('title_uk', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text_uk', models.TextField(max_length=2000, verbose_name='Текст')),
            ],
            options={
                'db_table': 'website_content_about',
                'verbose_name': 'Контент - Про нас',
                'verbose_name_plural': '               Контент - Про нас',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uk', models.CharField(max_length=100, verbose_name='Назва діяльності')),
                ('icon', models.CharField(max_length=30, verbose_name='Іконка')),
            ],
            options={
                'db_table': 'website_activities',
                'verbose_name': 'Вид діяльності',
                'verbose_name_plural': '          Види діяльності',
            },
        ),
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description_uk', models.CharField(max_length=1000, verbose_name='Короткий опис')),
            ],
            options={
                'db_table': 'website_centres',
                'verbose_name': 'Центр',
                'verbose_name_plural': '        Центри',
            },
            bases=(metadata.mixins.MetadataMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CentreSubpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline_uk', models.CharField(max_length=150, verbose_name='Назва сторінки')),
                ('content_uk', ckeditor.fields.RichTextField(verbose_name='Контент')),
                ('slug', models.SlugField(editable=False, max_length=150)),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='centres_subpages', to='website.Centre')),
            ],
            options={
                'db_table': 'website_centres_subpages',
                'verbose_name': 'Підсторінка Центру',
                'verbose_name_plural': '       Підсторінки Центрів',
            },
            bases=(metadata.mixins.MetadataMixin, models.Model),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', website.models.FixedStdImageField(upload_to=act.services.file_name.RandomFileName('cities/photos/'), verbose_name='Фотографія (головна)')),
                ('photo_square', website.models.FixedStdImageField(upload_to=act.services.file_name.RandomFileName('cities/photos/'), verbose_name='Фотографія (квадратна)')),
                ('photo_high', website.models.FixedStdImageField(upload_to=act.services.file_name.RandomFileName('cities/photos/'), verbose_name='Фотографія (висока)')),
                ('name_uk', models.CharField(max_length=100, unique=True, verbose_name='Назва')),
            ],
            options={
                'db_table': 'website_cities',
                'verbose_name': 'Місто',
                'verbose_name_plural': '         Міста',
            },
            bases=(metadata.mixins.MetadataMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=19, verbose_name='Телефон')),
                ('address_uk', models.CharField(blank=True, max_length=300, null=True, verbose_name='Адреса')),
                ('social_link', models.URLField(blank=True, null=True, verbose_name='Соціальна мережа')),
                ('centre', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Centre')),
            ],
            options={
                'db_table': 'website_contacts',
                'verbose_name': 'Контакт',
                'verbose_name_plural': '      Контакти',
            },
        ),
        migrations.CreateModel(
            name='DisclaimerContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text_uk', models.CharField(max_length=500, verbose_name='Дисклеймер українською')),
                ('text_en', models.CharField(max_length=500, verbose_name='Дисклеймер англійською')),
            ],
            options={
                'db_table': 'website_content_disclaimer',
                'verbose_name': 'Контент - Дисклеймер',
                'verbose_name_plural': '             Контент - Дисклеймер',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', website.models.FixedStdImageField(upload_to=act.services.file_name.RandomFileName('events/images/'), verbose_name='Головне зображення')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата та час')),
                ('title_uk', models.CharField(max_length=200, verbose_name='Назва')),
                ('content_uk', ckeditor.fields.RichTextField(verbose_name='Контент')),
                ('is_active', models.BooleanField(default=True, verbose_name='Відображається')),
                ('slug', models.SlugField(editable=False, max_length=200)),
            ],
            options={
                'db_table': 'website_events',
                'verbose_name': 'Матеріал',
                'ordering': ('-created_at', '-id'),
                'verbose_name_plural': '  Матеріали',
            },
            bases=(metadata.mixins.MetadataMixin, models.Model),
        ),
        migrations.CreateModel(
            name='EventAttachedDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(help_text='Дозволені типи файлів: .jpeg, .pdf, .doc, .docx, .xls, .xlsx, .ppt, .pptx\nМаксимальний розмір файлу: 5,0\xa0Мб', upload_to=website.models.attached_document_upload_to, validators=[act.validators.FileContentTypeValidator(allowed_content_types=('image/jpeg', 'application/pdf', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/vnd.ms-excel', 'application/octet-stream', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'application/vnd.ms-powerpoint', 'application/vnd.openxmlformats-officedocument.presentationml.presentation'), max_size=5242880)], verbose_name='Документ')),
                ('description_uk', models.CharField(max_length=200, verbose_name='Короткий опис')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_attached_documents', to='website.Event')),
            ],
            options={
                'db_table': 'website_events_attached_documents',
                'verbose_name': 'Прикріплений документ',
                'verbose_name_plural': 'Прикріплені документи',
            },
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uk', models.CharField(max_length=100, unique=True, verbose_name='Назва')),
            ],
            options={
                'db_table': 'website_events_categories',
                'verbose_name': 'Категорія матеріалу',
                'verbose_name_plural': '   Категорії матеріалів',
            },
        ),
        migrations.CreateModel(
            name='GoalContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('title_uk', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text_uk', models.TextField(max_length=2000, verbose_name='Текст')),
            ],
            options={
                'db_table': 'website_content_goal',
                'verbose_name': 'Контент - Мета',
                'verbose_name_plural': '              Контент - Мета',
            },
        ),
        migrations.CreateModel(
            name='IntroContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('headline_uk', models.CharField(max_length=200, verbose_name='Вступна фраза')),
            ],
            options={
                'db_table': 'website_content_intro',
                'verbose_name': 'Контент - Інтро',
                'verbose_name_plural': '                Контент - Інтро',
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', website.models.FixedStdImageField(upload_to=act.services.file_name.RandomFileName('participants/photos/'), verbose_name='Фотографія')),
                ('position_uk', models.CharField(max_length=100, verbose_name='Посада')),
                ('name_uk', models.CharField(max_length=200, verbose_name='Імʼя')),
                ('surname_uk', models.CharField(max_length=200, verbose_name='Прізвище')),
                ('centre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='participants', to='website.Centre')),
            ],
            options={
                'db_table': 'website_participants',
                'verbose_name': 'Співробітник',
                'verbose_name_plural': '      Співробітники',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', website.models.FixedStdImageField(upload_to=act.services.file_name.RandomFileName('partners/logos/'), verbose_name='Логотип')),
                ('name_uk', models.CharField(max_length=250, verbose_name='Назва компанії')),
                ('link', models.URLField(verbose_name='Посилання')),
            ],
            options={
                'db_table': 'website_partners',
                'verbose_name': 'Партнер',
                'verbose_name_plural': '         Партнери',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', website.models.FixedStdImageField(upload_to=act.services.file_name.RandomFileName('projects/images/'), verbose_name='Головне зображення')),
                ('title_uk', models.CharField(max_length=200, unique=True, verbose_name='Назва')),
                ('started_at', models.DateField(auto_now_add=True, verbose_name='Дата початку')),
                ('modified_at', models.DateField(default=django.utils.timezone.now, verbose_name='Дата оновлення')),
                ('content_uk', ckeditor.fields.RichTextField(verbose_name='Контент')),
                ('is_active', models.BooleanField(default=True, verbose_name='Відображається')),
                ('slug', models.SlugField(editable=False, max_length=200)),
            ],
            options={
                'db_table': 'website_projects',
                'verbose_name': 'Діяльність',
                'ordering': ('-modified_at', '-id'),
                'verbose_name_plural': '    Діяльності',
            },
            bases=(metadata.mixins.MetadataMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProjectArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uk', models.CharField(max_length=100, unique=True, verbose_name='Назва')),
            ],
            options={
                'db_table': 'website_projects_areas',
                'verbose_name': 'Напрямок діяльності',
                'verbose_name_plural': '     Напрямки діяльностей',
            },
        ),
        migrations.CreateModel(
            name='ProjectAttachedDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(help_text='Дозволені типи файлів: .jpeg, .pdf, .doc, .docx, .xls, .xlsx, .ppt, .pptx\nМаксимальний розмір файлу: 5,0\xa0Мб', upload_to=website.models.attached_document_upload_to, validators=[act.validators.FileContentTypeValidator(allowed_content_types=('image/jpeg', 'application/pdf', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/vnd.ms-excel', 'application/octet-stream', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'application/vnd.ms-powerpoint', 'application/vnd.openxmlformats-officedocument.presentationml.presentation'), max_size=5242880)], verbose_name='Документ')),
                ('description_uk', models.CharField(max_length=200, verbose_name='Короткий опис')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_attached_documents', to='website.Project')),
            ],
            options={
                'db_table': 'website_projects_attached_documents',
                'verbose_name': 'Прикріплений документ',
                'verbose_name_plural': 'Прикріплені документи',
            },
        ),
        migrations.CreateModel(
            name='Scraping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=500)),
                ('head', models.TextField()),
            ],
            options={
                'db_table': 'website_scrapings',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Назва мережі')),
                ('link', models.URLField(verbose_name='Посилання')),
                ('icon', models.CharField(max_length=30, verbose_name='Іконка')),
            ],
            options={
                'db_table': 'website_socials',
                'verbose_name': 'Соціальна мережа',
                'verbose_name_plural': '           Соціальні мережі',
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to=act.services.file_name.RandomFileName('sponsors/logos/'), verbose_name='Логотип')),
                ('title_uk', models.CharField(max_length=100, verbose_name='Назва організації')),
                ('link', models.URLField(verbose_name='Посилання')),
            ],
            options={
                'db_table': 'website_sponsors',
                'verbose_name': 'Донор',
                'verbose_name_plural': '            Донори',
            },
        ),
        migrations.CreateModel(
            name='Worksheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=300, verbose_name='ПІБ')),
                ('residence', models.CharField(max_length=500, verbose_name='Місце проживання')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=19, verbose_name='Телефон')),
                ('personal_link', models.URLField(blank=True, null=True, verbose_name='Персональна сторінка')),
                ('problem', models.NullBooleanField(verbose_name='Бажаєте повідомити про проблему?')),
                ('problem_description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Із якою проблемою Вам довелося зіштовхнутися?')),
                ('activity', models.NullBooleanField(verbose_name='Чи бажаєте Ви долучитись до «ДІЙ!»?')),
                ('activity_description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='У якій діяльності в рамках «ДІЙ!» ви би хотіли взяти участь?')),
            ],
            options={
                'db_table': 'website_worksheet',
                'verbose_name': 'Анкета',
                'verbose_name_plural': ' Анкети',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='project_area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='website.ProjectArea'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='website.EventCategory'),
        ),
        migrations.AddField(
            model_name='event',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='website.Project'),
        ),
        migrations.AddField(
            model_name='centre',
            name='city',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.City'),
        ),
        migrations.AddField(
            model_name='centre',
            name='events',
            field=models.ManyToManyField(blank=True, related_name='centres', to='website.Event'),
        ),
        migrations.AddField(
            model_name='centre',
            name='projects',
            field=models.ManyToManyField(blank=True, related_name='centres', to='website.Project'),
        ),
        migrations.AddField(
            model_name='centre',
            name='top_event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.Event'),
        ),
    ]

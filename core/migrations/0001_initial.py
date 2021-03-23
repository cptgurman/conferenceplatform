# Generated by Django 3.1.6 on 2021-03-19 15:40

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_name', models.CharField(max_length=500, verbose_name='Корпус')),
                ('building_adress', models.CharField(max_length=500, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Корпус',
                'verbose_name_plural': 'Корпусы',
            },
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conference_name', models.CharField(max_length=200, verbose_name='Краткое название')),
                ('conference_full_name', models.CharField(max_length=500, verbose_name='Полное название')),
                ('conference_format_id', models.CharField(choices=[('Ochnoe', 'Очное'), ('Zaochnoe', 'Заочное'), ('OchZaoch', 'Очно-заочное')], max_length=500, verbose_name='Формат проведения конференции')),
                ('conference_date_start', models.DateField(verbose_name='Дата начала конференции')),
                ('conference_date_end', models.DateField(verbose_name='Дата окончания конференции')),
                ('conference_date_reg_start', models.DateField(verbose_name='Дата начала регистрации')),
                ('conference_date_reg_end', models.DateField(verbose_name='Дата окончания регистрации')),
                ('conference_discription', models.TextField(verbose_name='Описание')),
                ('conference_building_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.building', verbose_name='Корпус')),
            ],
            options={
                'verbose_name': 'Конференция',
                'verbose_name_plural': 'Конференции',
            },
        ),
        migrations.CreateModel(
            name='ConferenceSections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conference_sections_name', models.CharField(max_length=50, verbose_name='Название секции')),
                ('conference_sections_conference_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.conference', verbose_name='Конференция')),
            ],
            options={
                'verbose_name': 'Секция',
                'verbose_name_plural': 'Секции',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
            ],
            options={
                'verbose_name': 'Пользователь_прокси',
                'verbose_name_plural': 'Пользователи_прокси',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='MemberInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memberinfo_surname', models.CharField(max_length=500, verbose_name='Фамилия')),
                ('memberinfo_name', models.CharField(max_length=500, verbose_name='Имя')),
                ('memberinfo_otchestvo', models.CharField(max_length=500, verbose_name='Отчество')),
                ('memberinfo_dateofbirth', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('memberinfo_telephone', models.CharField(max_length=500, verbose_name='Номер телефона')),
                ('memberinfo_job_telephone', models.CharField(max_length=500, verbose_name='Рабочий телефон')),
                ('memberinfo_dolshnost', models.CharField(max_length=500, verbose_name='Должность')),
                ('memberinfo_education', models.CharField(max_length=500, verbose_name='Образование')),
                ('memberinfo_achievements', models.TextField(verbose_name='Научные достижения')),
                ('memberinfo_male', models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский')], default='M', max_length=500, verbose_name='Пол')),
                ('memberinfo_OKS', models.CharField(max_length=500, verbose_name='Основной код классификатора')),
                ('memberinfo_DOPOKS', models.CharField(max_length=500, verbose_name='Дополнительные коды классификатора')),
                ('memberinfo_OKVED', models.CharField(max_length=500, verbose_name='Раздел ОКВЭД')),
                ('memberinfo_gradee', models.CharField(choices=[('Candidate', 'Кондидат наук'), ('Doctor', 'Доктор наук'), ('NO', 'Отсутсвует')], default='NO', max_length=500, verbose_name='Ученое степень')),
                ('memberinfo_gradee_name', models.CharField(choices=[('Docent', 'Доцент'), ('Professor', 'Профессор'), ('NO', 'Отсутсвует')], default='NO', max_length=500, verbose_name='Ученое звание')),
                ('memberinfo_user', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.member', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Информация об участнике',
                'verbose_name_plural': 'Информация об участниках',
            },
        ),
        migrations.CreateModel(
            name='MemberApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speech_file', models.FileField(upload_to='', verbose_name='Файл')),
                ('app_status', models.CharField(choices=[('Consideration', 'На рассмотрении'), ('Denial', 'Отказ'), ('Approved', 'Одобрено'), ('Revision', 'На доработку')], default='Consideration', max_length=100, verbose_name='Статус рассмотрения')),
                ('expert_app_comment', models.TextField(blank=True, verbose_name='Комментарий')),
                ('participation_form', models.CharField(choices=[('Ochnoe', 'Очное'), ('Zaochnoe', 'Заочное'), ('OchZaoch', 'Очно-заочное')], max_length=100, verbose_name='Формат участия в конференции')),
                ('co_authors', models.TextField(max_length=500, verbose_name='Соавторы')),
                ('speech_name', models.CharField(max_length=100, verbose_name='Название темы')),
                ('speech_keywords', models.CharField(max_length=100, verbose_name='Ключевые слова')),
                ('speech_annotation', models.TextField(max_length=1000, verbose_name='Аннотация')),
                ('hotel_required', models.BooleanField(blank=True, verbose_name='Гостиница')),
                ('invitation_required', models.BooleanField(blank=True, verbose_name='Приглашение')),
                ('conference_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.conference', verbose_name='Конференция')),
                ('expert', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='expert', to='core.member', verbose_name='Эксперт')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='member', to='core.member', verbose_name='Участник')),
                ('member_section', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.conferencesections', verbose_name='Секция')),
            ],
            options={
                'verbose_name': 'Приложения к участнику',
                'verbose_name_plural': 'Приложения к участникам',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=500, verbose_name='Факультет')),
                ('faculty_building_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.building', verbose_name='Корпус')),
            ],
            options={
                'verbose_name': 'Факультет',
                'verbose_name_plural': 'Факультеты',
            },
        ),
        migrations.CreateModel(
            name='ExpertKeywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.TextField(blank=True, verbose_name='Ключевые слова эксперта')),
                ('expert', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='core.member', verbose_name='Эксперт')),
            ],
            options={
                'verbose_name': 'Ключевые слова эксперта',
            },
        ),
        migrations.CreateModel(
            name='ExpertArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.FileField(blank=True, upload_to='', verbose_name='Docx файл со статьей')),
                ('article_keywords', models.TextField(blank=True, verbose_name='Ключевые слова статьи')),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.member', verbose_name='Эксперт')),
            ],
            options={
                'verbose_name': 'Статьи эксперта',
            },
        ),
        migrations.AddField(
            model_name='conference',
            name='conference_faculty_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.faculty', verbose_name='Факультет'),
        ),
        migrations.AddField(
            model_name='conference',
            name='conference_org_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.member', verbose_name='Организатор'),
        ),
    ]

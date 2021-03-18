from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist

class ConferenceQuerySet(models.QuerySet):
    def ochnye(self):
        return self.filter(format_id='Ochnoe')
    
    def reg_open(self):
        return self.filter()

class Member(User):
    class Meta:
        proxy = True
        verbose_name= "Пользователь_прокси"
        verbose_name_plural= "Пользователи_прокси"

GENDERS = (
        ('M','Мужской'),
        ('F','Женский'),
    )

STEPENI = (
        ('Candidate','Кондидат наук'),
        ('Doctor','Доктор наук'),
        ('NO','Отсутсвует'),
    )
ZVANIE = (
        ('Docent','Доцент'),
        ('Professor','Профессор'),
        ('NO','Отсутсвует'),
    )
FORMAT = (
        ('Ochnoe','Очное'),
        ('Zaochnoe','Заочное'),
        ('OchZaoch','Очно-заочное')
    )

Member_STATUS = (
    ('Consideration','На рассмотрении'),
    ('Denial','Отказ'),
    ('Approved','Одобрено'),
    ('Revision','На доработку')
)

Conference_STATUS = (
    ('Open','Открытая'),
    ('Close','Закрытая'),
    ('Deferred','Отложенная'),
)



class Building (models.Model):
    building_name=models.CharField("Корпус", max_length=500,)
    building_adress=models.CharField("Адрес", max_length=500)

    class Meta:
        verbose_name= "Корпус"
        verbose_name_plural="Корпусы"
    def __str__(self):
        return str(self.building_name)


class Faculty (models.Model):
    
    faculty_name=models.CharField("Факультет", max_length=500)
    faculty_building_id=models.ForeignKey(Building, on_delete=models.PROTECT, verbose_name= "Корпус")
    
    class Meta:
        verbose_name= "Факультет"
        verbose_name_plural="Факультеты" 

    def __str__(self):
        return str(self.faculty_name)


class MemberInfo (models.Model):
    memberinfo_user = models.OneToOneField(Member, on_delete=models.CASCADE,default=None, null=True, verbose_name='Пользователь')
    memberinfo_surname=models.CharField(max_length=500, verbose_name='Фамилия')
    memberinfo_name=models.CharField(max_length=500, verbose_name='Имя')
    memberinfo_otchestvo=models.CharField(max_length=500, verbose_name='Отчество')
    memberinfo_dateofbirth=models.DateField(verbose_name='Дата рождения',  null=True, blank=True)
    memberinfo_telephone=models.CharField(max_length=500, verbose_name='Номер телефона')
    memberinfo_job_telephone=models.CharField(max_length=500, verbose_name='Рабочий телефон')
    memberinfo_dolshnost=models.CharField(max_length=500, verbose_name='Должность')
    memberinfo_education=models.CharField(max_length=500, verbose_name='Образование')
    memberinfo_achievements=models.TextField(verbose_name='Научные достижения')
    memberinfo_male=models.CharField(max_length=500, choices=GENDERS, verbose_name='Пол', default='M')
    memberinfo_OKS=models.CharField(max_length=500, verbose_name='Основной код классификатора')
    memberinfo_DOPOKS=models.CharField(max_length=500, verbose_name='Дополнительные коды классификатора')
    memberinfo_OKVED=models.CharField(max_length=500, verbose_name='Раздел ОКВЭД')
    memberinfo_gradee=models.CharField(max_length=500, choices=STEPENI, verbose_name='Ученое степень', default='NO')
    memberinfo_gradee_name=models.CharField(max_length=500, verbose_name='Ученое звание', choices=ZVANIE, default='NO')


    def __str__(self):
        return str(self.memberinfo_user)
    class Meta:
        verbose_name= "Информация об участнике"
        verbose_name_plural= "Информация об участниках"

    def get_absolute_url(self):  # Ссылка на страницу после выхода
        return reverse('lk')


class Conference (models.Model):
    conference_org_id=models.ForeignKey(Member, on_delete=models.PROTECT, verbose_name='Организатор')
    conference_name = models.CharField(max_length=200, verbose_name='Краткое название',) 
    conference_full_name=models.CharField(max_length=500, verbose_name='Полное название',)
    conference_format_id=models.CharField(max_length=500, choices=FORMAT, verbose_name='Формат проведения конференции')
    conference_date_start=models.DateField(verbose_name='Дата начала конференции')
    conference_date_end=models.DateField(verbose_name='Дата окончания конференции')
    conference_date_reg_start=models.DateField(verbose_name='Дата начала регистрации')
    conference_date_reg_end=models.DateField(verbose_name='Дата окончания регистрации')
    conference_discription=models.TextField(verbose_name='Описание')
    conference_faculty_id=models.ForeignKey(Faculty, on_delete=models.PROTECT, verbose_name='Факультет')
    conference_building_id=models.ForeignKey(Building, on_delete=models.PROTECT, verbose_name='Корпус')

    objects = ConferenceQuerySet.as_manager()

    class Meta:
        verbose_name= "Конференция"
        verbose_name_plural="Конференции"
        

    def __str__(self):
        return str(self.conference_name)

    def get_absolute_url(self):  # Ссылка на страницу после выхода
        return reverse('lk')


class ConferenceSections (models.Model):
    conference_sections_conference_id = models.ForeignKey(Conference,on_delete=models.PROTECT, verbose_name='Конференция')
    conference_sections_name=models.CharField(max_length=50, verbose_name='Название секции')

    def __str__(self):
        return str(self.conference_sections_name)

    class Meta:
        verbose_name= "Секция"
        verbose_name_plural="Секции"


class MemberApplication (models.Model):
    member=models.ForeignKey(Member, on_delete=models.PROTECT,related_name='member', verbose_name='Участник')
    conference_id=models.ForeignKey(Conference, on_delete=models.PROTECT, verbose_name='Конференция')
    speech_file=models.FileField(verbose_name='Файл')
    app_status=models.CharField(max_length=100, choices=Member_STATUS,verbose_name='Статус рассмотрения', default='Consideration')
    expert_app_comment=models.TextField(verbose_name='Комментарий',blank=True)
    participation_form=models.CharField(max_length=100, choices=FORMAT, verbose_name='Формат участия в конференции')
    member_section=models.ForeignKey(ConferenceSections, on_delete=models.PROTECT, verbose_name='Секция')
    expert=models.ForeignKey(Member, on_delete=models.PROTECT, related_name='expert', verbose_name='Эксперт', null=True)
    co_authors=models.TextField(max_length=500, verbose_name='Соавторы')
    speech_name=models.CharField(max_length=100, verbose_name='Название темы')
    speech_keywords=models.CharField(max_length=100, verbose_name='Ключевые слова')
    speech_annotation=models.TextField(max_length=1000, verbose_name='Аннотация')
    hotel_required=models.BooleanField(verbose_name='Гостиница', blank=True)
    invitation_required=models.BooleanField(verbose_name='Приглашение', blank=True)
   

    def __str__(self):
        return str(self.member)
    class Meta:
        verbose_name= "Приложения к участнику"
        verbose_name_plural="Приложения к участникам"


class ExpertKeywords(models.Model):
    expert=models.OneToOneField(Member, on_delete=models.PROTECT, verbose_name='Эксперт')
    keywords=models.TextField(verbose_name='Ключевые слова эксперта', blank=True)

    class Meta:
        verbose_name = "Ключевые слова эксперта"

    def __str__(self):
        return str(self.keywords)


class ExpertArticle(models.Model):
    expert = models.ForeignKey(Member, on_delete=models.PROTECT, verbose_name='Эксперт' )
    article=models.FileField(verbose_name='Docx файл со статьей', blank=True)
    article_keywords=models.TextField(verbose_name='Ключевые слова статьи', blank=True)

    class Meta:
        verbose_name = "Статьи эксперта"

    def __str__(self):
        return str(self.expert)

    

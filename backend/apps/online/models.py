from django.db import models



class Organizations(models.Model):
    text_name = models.CharField("Организационно-правовая форма", max_length=50)

    def __str__(self):
        return self.text_name

    class Meta:
        verbose_name = 'форма'
        verbose_name_plural = 'формы'

class Sector(models.Model):
    title_name = models.CharField("Сектор", max_length=250)

    def __str__(self):
        return self.title_name

    class Meta:
        verbose_name = 'Сектор'
        verbose_name_plural = 'Сектора'

class Region(models.Model):
    region_name = models.CharField("Область", max_length=250)

    def __str__(self):
        return self.region_name

    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = 'Область'


class Create(models.Model):
    organ_name = models.CharField("Наименование хозяйствующего субъекта", max_length=255)
    inn = models.DecimalField("ИНН", max_digits=255, decimal_places=0, unique=True)

    organizations = models.ForeignKey(Organizations, verbose_name="Организационно-правовая форма", on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, verbose_name="Отрасль/Сектор", on_delete=models.CASCADE)
    region = models.ForeignKey(Region, verbose_name="Область", on_delete=models.CASCADE)
    city = models.CharField("Город/Село", max_length=200)
    adress = models.CharField("Адрес", max_length=200)

    supervisor_last_name = models.CharField("Фамилия", max_length=50)
    supervisor_first_name = models.CharField("Имя", max_length=50)
    supervisor_middle_name = models.CharField("Отчество", max_length=50, blank=True, null=True)
    supervisor_job_title = models.CharField("Должность", max_length=50)
    supervisor_phone = models.DecimalField("Номер телефона", max_digits=255, decimal_places=0)

    file_before = models.FileField(upload_to='file', blank=True, null=True)
    file_rear = models.FileField(upload_to='file', blank=True, null=True)

    last_name = models.CharField("Фамилия", max_length=50)
    first_name = models.CharField("Имя", max_length=50)
    middle_name = models.CharField("Отчество", max_length=50)
    job_title = models.CharField("Должность", max_length=50)
    phone = models.DecimalField("Номер телефона", max_digits=255, decimal_places=0)
    email = models.EmailField("Почта")

    requested_amount = models.IntegerField("Запрашиваемая сумма", max_length=255)
    credit_term = models.CharField("Срок кредита", max_length=255, default="")
    target_direction = models.CharField("Целевое направление кредита", max_length=255)
    own_contribution = models.CharField("обственный вклад в денежном выражении", max_length=255)
    desired_schedule = models.CharField("Желаемый график погашения", max_length=255)

    doc_title = models.CharField("Наименование документа", max_length=255)
    location = models.CharField("Месторасположение", max_length=255)
    indicative = models.CharField("Ориентировочная оценочная стоимость", max_length=255)
    owner = models.CharField("Собственник", max_length=255)
    file = models.FileField(upload_to='file', blank=True, null=True)

    business_plan = models.CharField("Бизнес план", max_length=255)
    financial_statements = models.CharField("Финансовая отчетность", max_length=255)
    certificate = models.CharField("Свидетельство о госрегистрации", max_length=255)
    founding_document = models.CharField("Учредительный документ", max_length=255)
    entitlement = models.CharField("Правоустанавливающий", max_length=255)
    is_active = models.BooleanField("Согласие", default=True)
    is_actives = models.BooleanField("Ознакомлен ", default=True)
    created = models.DateField(verbose_name="Дата создание", auto_now_add=True)


    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Онлайн заявка'
        verbose_name_plural = 'Онлайн заявки'    



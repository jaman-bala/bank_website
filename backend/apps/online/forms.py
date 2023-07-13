from .models import Create
from django.forms import (ModelForm, TextInput, 
                          DateTimeInput, Textarea, 
                          FileInput, Select, DecimalField, 
                          EmailInput, IntegerField)



class CreateForm(ModelForm):
    class Meta:
        model = Create
        fields = ['organ_name', 'inn', 'organizations', 'sector' ,'region', 
        'city', 'adress', 'supervisor_last_name', 'supervisor_first_name', 'supervisor_middle_name', 
        'supervisor_job_title', 'supervisor_phone', 'file_before', 'file_rear', 'last_name', 'first_name', 
        'middle_name', 'job_title', 'phone', 'email', 'requested_amount', 'credit_term', 'target_direction', 
        'own_contribution', 'desired_schedule', 'doc_title', 'location', 'indicative', 'owner', 'file', 
        'business_plan', 'financial_statements', 'certificate', 'founding_document', 'entitlement', 
        'is_active', 'is_actives']

        widgets = {
                #Информация об организации
            "organ_name": TextInput(attrs={
              
                'placeholder': 'Наименование хозяйствующего субъекта'
            }),
            "inn": TextInput(attrs={
              
                'placeholder': 'ИНН'
            }),
            "organizations": Select(attrs={
              
                'placeholder': 'Организационно-правовая форма'
            }),
            "sector": Select(attrs={
              
                'placeholder': 'Отрасль/Сектор'
            }),
            "region": Select(attrs={
              
                'placeholder': 'Область'
            }),
            "city": TextInput(attrs={
              
                'placeholder': 'Город/Село'
            }),
            "adress": TextInput(attrs={
              
                'placeholder': 'Адрес'
            }),


                #Информация о руководителе
            "supervisor_last_name": TextInput(attrs={
              
                'placeholder': 'Фамилия'
            }),
            "supervisor_first_name": TextInput(attrs={
              
                'placeholder': 'Имя'
            }),
            "supervisor_middle_name": TextInput(attrs={
              
                'placeholder': 'Отчество'
            }),
            "supervisor_job_title": TextInput(attrs={
              
                'placeholder': 'Должность'
            }),
            "supervisor_phone": TextInput(attrs={
              
                'placeholder': 'Номер телефона'
            }),
            "file_before": FileInput(attrs={
              
                'placeholder': 'file'
            }),
            "file_rear": FileInput(attrs={
              
                'placeholder': 'file'
            }),

                #Контактное лицо
             "last_name": TextInput(attrs={
              
                'placeholder': 'Фамилия'
            }),
            "first_name": TextInput(attrs={
              
                'placeholder': 'Имя'
            }),
            "middle_name": TextInput(attrs={
              
                'placeholder': 'Отчество'
            }),
            "job_title": TextInput(attrs={
              
                'placeholder': 'Должность'
            }),
            "phone": TextInput(attrs={
              
                'placeholder': 'Номер телефона'
            }),
            "email": EmailInput(attrs={
              
                'placeholder': 'Email'
            }),


            "requested_amount": IntegerField(attrs={
              
                'placeholder': 'Запрашиваемая сумма'
            }),

        }
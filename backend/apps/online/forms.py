from .models import Create
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileInput



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
            "first_name": TextInput(attrs={
              
                'placeholder': 'Имя'
            }),
            "last_name": TextInput(attrs={
    
                'placeholder': 'Фамилия'
            }),
            "phone": TextInput(attrs={

                'placeholder': '+996 '
            }),
            "email": TextInput(attrs={

                'placeholder': 'Адрес электронной почты'
            }),
            "city": TextInput(attrs={

                'placeholder': 'Адрес'
            }),


            "file": FileInput(attrs={

                'placeholder': 'Файл'
            }),


        }
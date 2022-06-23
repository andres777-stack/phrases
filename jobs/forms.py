from datetime import datetime
from django import forms #forms es un folder. 
from django.core.exceptions import ValidationError
from  .models import Applicant

def validate_checked(value):
    if not value:
        raise ValidationError("Required")

class JobApplicationForm(forms.ModelForm):
    
    DAYS = (
        (1, 'MON'),
        (2, 'TUE'),
        (3, 'WED'),
        (4, 'THU'),
        (5, 'FRI')
    )

    available_days = forms.TypedMultipleChoiceField(
        choices=DAYS,
        coerce=int,
        help_text = 'Check all days that you can work.',
        widget = forms.CheckboxSelectMultiple(
            attrs = {'checked':True}
        )
    )

    confirmation = forms.BooleanField(
        label = 'I certify that the information I have provided is true.',
        validators=[validate_checked]
    )

    class Meta:
        model = Applicant
        fields = (
            'first_name', 'last_name', 'email', 'website', 'employment_type',
            'start_date', 'available_days', 'desired_hourly_wage',
            'cover_letter', 'resume', 'confirmation', 'job')
        widgets = {
            'first_name': forms.TextInput(attrs={'autofocus': True}),
            'website': forms.TextInput(
                attrs = {'placeholder':'https://www.example.com'}
            ),
            'start_date': forms.SelectDateWidget(
                attrs = {
                    'style': 'width: 31%; display: inline-block; margin: 0 1%'
                },
                years = range(datetime.now().year, datetime.now().year+2)
            ),
            'desired_hourly_wage': forms.NumberInput(
                attrs = {'min':'10.00', 'max':'100.00', 'step':'.25'}
            ),
            'cover_letter': forms.Textarea(attrs={'cols': '100', 'rows': '5'}), 
            'resume': forms.FileInput(attrs={'accept': 'application/pdf'}),
        }
        error_messages = {
            'start_date': {
                'past_date': 'Please enter a future date.'
            }
        }


    #YEARS = range(1900, datetime.now().year + 1) #Como range excluye el último valor, es necesario poner más 1. 


    #Forms es una clase integrada en el folder forms de forms. Se puede acceder así por el init. 
    #first_name = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
    #last_name = forms.CharField()
    #email = forms.EmailField()
    #website = forms.URLField(widget=forms.URLInput(attrs={'placeholder': 'https://www.example.com', 'size':'50'}), required=False)
    #employment_type = forms.ChoiceField()
    #start_date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS, attrs={'style': 'width: 31%; display: inline-block; margin: 0 1%'}), validators=[validate_future_date], 
    #error_messages = {'past_date' : 'Please enter a future date.'}, help_text='The earliest date you can start working')
    #available_days = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'checked': True}), choices=DAYS, help_text='Select all days that you can work')
    #desired_hourly_wage = forms.DecimalField(widget=forms.NumberInput(attrs={'min': '10.00', 'max':'100.00', 'step':'5'}))
    #cover_letter = forms.CharField(widget=forms.Textarea(attrs={'cols':'75', 'rows':'15'}))
    #confirmation = forms.BooleanField(label='I certify that the information I have provided is true')
    #hasta aquí lo que se ha creado es una clase con atributos. 


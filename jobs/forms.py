from datetime import datetime
from django import forms #forms es un folder. 


class JobApplicationForm(forms.Form): 
    EMPLOYMENT_TYPE = (
    (None, '--please choose--'),
    ('ft', 'Full-Time'),
    ('pt', 'Part-Time'),
    ('contract', 'Contract-work')
    )

    DAYS = (
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday')
    )

    YEARS = range(1900, datetime.now().year + 1) #Como range excluye el último valor, es necesario poner más 1. 

    #Forms es una clase integrada en el folder forms de forms. Se puede acceder así por el init. 
    first_name = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(widget=forms.URLInput(attrs={'placeholder': 'https://www.example.com', 'size':'50'}), required=False)
    employment_type = forms.ChoiceField(choices=EMPLOYMENT_TYPE)
    start_date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS), help_text='The earliest date you can start working')
    available_days = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'checked': True}), choices=DAYS, help_text='Select all days that you can work')
    desired_hourly_wage = forms.DecimalField(widget=forms.NumberInput(attrs={'min': '10.00', 'max':'100.00', 'step':'5'}))
    cover_letter = forms.CharField(widget=forms.Textarea(attrs={'cols':'75', 'rows':'15'}))
    confirmation = forms.BooleanField(label='I certify that the information I have provided is true')
    #hasta aquí lo que se ha creado es una clase con atributos. 


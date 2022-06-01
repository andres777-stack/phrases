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

    #Forms es una clase integrada en el folder forms de forms. Se puede acceder así por el init. 
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(required=False)
    employment_type = forms.ChoiceField(choices=EMPLOYMENT_TYPE)
    start_date = forms.DateField(help_text='The earliest date you can start working')
    available_days = forms.MultipleChoiceField(choices=DAYS, help_text='Select all days that you can work')
    desired_hourly_wage = forms.DecimalField()
    cover_letter = forms.CharField()
    confirmation = forms.BooleanField(label='I certify that the information I have provided is true')
    #hasta aquí lo que se ha creado es una clase con atributos. 


from django import forms #forms es un folder. 

class JobApplicationForm(forms.Form): 
    #Forms es una clase integrada en el folder forms de forms. Se puede acceder así por el init. 
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    #hasta aquí lo que se ha creado es una clase con atributos. 


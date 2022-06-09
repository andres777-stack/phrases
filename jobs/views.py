import html #funciones para manipulación de elementos html.
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, CreateView

from common.utils.email import send_email
from jobs.models import Applicant, Job
from .forms import JobApplicationForm

class JobAppView(CreateView):
    model = Applicant
    template_name = 'jobs/applicant_form.html' #indica el template para renderizar el formulario. 
    form_class = JobApplicationForm #identifica la clase Form, que contiene los fields a ser mostrados.
    success_url = reverse_lazy('jobs:thanks') # luego que el formulario es procesado, se redireccionará a esta url.
    '''
    Por debajo, el context contendrá una instancia 'form' de la clase JobApplicationForm, conl los tres fields añadidos en
    forms.py.
    '''
    def form_valid(self, form):
        data = form.cleaned_data #Es un diccionario, que será poblado con las k, v proveniente del formulario.
        to = 'sergioramirezsanmartin@gmail.com'
        subject = 'Application por Phrase Writer'
        content = f'''<p>Hey HR Manager!</p>
            <p>Job Application received:</p>
            <ol>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title() #reemplaza _ por espacio y transforma la primera letra en mayuscula.
            entry = html.escape(str(value), quote=False)#Escapa del proceso los elementos HTML riesgosos, no las ''.
            content += f'<li>{label}: {entry}</li>'
        content +='</ol>'
        send_email(to, subject, content)
        return super().form_valid(form) #now, do your stuff(redirect). Cada vez que se sobreescribe un método, es necesario esto.
#Aquí se está sobrescribiendo la función que redirige a una pagina success. Pero antes de que se redireccione, 
#_se envía un correo electrónico al Gerente de RRHH. 
        

class JobAppThanksView(TemplateView):
    template_name = 'jobs/thanks.html'


# Create your views here.

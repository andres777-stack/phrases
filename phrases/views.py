from django.views.generic import ListView
from .models import Phrase

class PhraseListView(ListView):
    model = Phrase

# Create your views here.

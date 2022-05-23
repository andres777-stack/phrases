from django.views.generic import ListView, DetailView
from .models import Phrase

class PhraseListView(ListView):
    model = Phrase

class PhraseDetailView(DetailView):
    model = Phrase
# Create your views here.

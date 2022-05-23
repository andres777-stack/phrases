from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Phrase

class PhraseListView(ListView):
    model = Phrase

class PhraseDetailView(DetailView):
    model = Phrase

class PhraseCreateView(CreateView):
    model = Phrase
    fields = ['sentence', 'author']

class PhraseUpdateView(UpdateView):
    model = Phrase
    fields = ['sentence', 'author']
# Create your views here.

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Phrase
from django.urls import reverse_lazy

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

class PhraseDeleteView(DeleteView):
    model = Phrase
    success_url = reverse_lazy('phrases:list')

# Create your views here.

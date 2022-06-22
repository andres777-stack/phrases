from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Phrase
from .forms import PhraseForm
from django.urls import reverse_lazy

class PhraseListView(ListView):
    model = Phrase

class PhraseDetailView(DetailView):
    model = Phrase

class PhraseCreateView(CreateView):
    model = Phrase
    form_class = PhraseForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PhraseUpdateView(UpdateView):
    model = Phrase
    form_class = PhraseForm

class PhraseDeleteView(DeleteView):
    model = Phrase
    success_url = reverse_lazy('phrases:list')

# Create your views here.

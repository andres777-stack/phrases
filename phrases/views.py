from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Phrase
from .forms import PhraseForm
from django.urls import reverse_lazy

class PhraseListView(ListView):
    model = Phrase

class PhraseDetailView(DetailView):
    model = Phrase

class PhraseCreateView(LoginRequiredMixin, CreateView):
    model = Phrase
    form_class = PhraseForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PhraseUpdateView(UserPassesTestMixin, UpdateView):
    model = Phrase
    form_class = PhraseForm

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user

class PhraseDeleteView(UserPassesTestMixin, DeleteView):
    model = Phrase
    success_url = reverse_lazy('phrases:list')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user

# Create your views here.

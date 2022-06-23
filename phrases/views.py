
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Phrase
from .forms import PhraseForm
from django.urls import reverse_lazy

class PhraseListView(ListView):
    model = Phrase

class PhraseDetailView(DetailView):
    model = Phrase

class PhraseCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Phrase
    form_class = PhraseForm
    success_message = 'Phrase created successfully.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PhraseUpdateView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Phrase
    form_class = PhraseForm
    success_message = 'Update successful.'

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user

class PhraseDeleteView(UserPassesTestMixin, DeleteView):
    model = Phrase
    success_url = reverse_lazy('phrases:list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Phrase deleted.')
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user
    
    

# Create your views here.

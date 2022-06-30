
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Phrase, PhraseVote
from .forms import PhraseForm
from django.urls import reverse_lazy
import json
from django.http import JsonResponse

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

def vote(request, slug):
    user = request.user
    phrase = Phrase.objects.get(slug=slug)
    data = json.loads(request.body)
    vote = data['vote']
    likes = data['likes']
    dislikes = data['dislikes']

    if user.is_anonymous:
        msg = 'Sorry, you have to be logged in to vote.'
    else:
        if PhraseVote.objects.filter(user=user, phrase=phrase).exists():
            phrase_vote = PhraseVote.objects.get(user=user, phrase=phrase)
            if phrase_vote.vote == vote:
                msg = 'Rigth. You told us already. Geez.'
            else:
                phrase_vote.vote = vote
                phrase_vote.save()

                if vote == -1:
                    likes -= 1
                    dislikes += 1
                    msg = 'Dont like it after all, huh? Ok. Noted'
                else:
                    likes += 1
                    dislikes -= 1
                    msg = 'Grown on you, has it? Ok. Noted.'
        else:
            phrase_vote = PhraseVote(user=user, phrase=phrase, vote=vote)
            phrase_vote.save()
            if vote == -1:
                dislikes += 1
                msg = 'Sorry, you did not like the joke.'
            else:
                likes += 1
                msg = 'Yeah, good one, rigth?'
        response = {'msg':msg, 'likes':likes, 'dislikes':dislikes}
    return JsonResponse(response)







# Create your views here.

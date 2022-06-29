
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
    user = request.user #el usuario logado o el anonimususer. Notar la fuente del usuario.
    phrase = Phrase.objects.get(slug=slug) #la instancia de frase.
    data = json.loads(request.body) #Data proveniente de Js.
    vote = data['vote'] #The user's new vote.
    likes = data['likes']#the numbers of likes currently displayed on page.
    dislikes = data['dislikes']#the number of dislikes currently displayed.

    if user.is_anonymous: #can't vote 
        msg = 'Sorry, you have to be logged in to vote.'
    else: #user is logged.
        if PhraseVote.objects.filter(user=user, phrase=phrase).exists():
            #user alrady voted. Get user's past vote:
            phrase_vote = PhraseVote.objects.get(user=user, phrase=phrase)
            if phrase_vote.vote == vote:
                #User's new vote is the same as old vote.
                msg = 'Right. You told us already. Geez'
            else:
                #User change the vote.
                phrase_vote.vote = vote
                phrase_vote.save()

                if vote == -1:
                    likes -= 1
                    dislikes += 1
                    msg = "Don't like it after all, huh? Ok. Noted."
                else:
                    likes += 1
                    dislikes -= 1
                    msn = 'Grown on you, has it? Ok. Noted.'
        else:
            #Primera vez que el usuario vota en esta frase.
            #crear y guardar un nuevo voto.
            phrase_vote = PhraseVote(user=user, phrase=phrase, vote=vote)
            phrase_vote.save()
            #Configurando los datos para retornar al navegador.
            if vote == -1:
                dislikes += 1
                msg = 'Sorry you did not like the phrase'
            else:
                likes += 1
                msn = 'Yeah, good one, right?'

        #creando un objeto para retornar al nevegador
        response = {
            'msg' : msg,
            'likes': likes,
            'dislikes': dislikes,
        }
        return JsonResponse(response) #return object as Json. 







# Create your views here.

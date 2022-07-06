
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Phrase, PhraseVote
from .forms import PhraseForm
from django.urls import reverse_lazy
import json
from django.http import JsonResponse
from django.db.models import Q

class PhraseListView(ListView):
    model = Phrase
    paginate_by = 4

    def get_order_settings(self):
        order_fields = self.get_order_fields()
        default_order_key = order_fields['default_key']
        order_key = self.request.GET.get('order', default_order_key)
        direction = self.request.GET.get('direction', 'desc')
        #if order_key is invalid, use default.
        if order_key not in order_fields:
            order_key = default_order_key
        return (order_fields, order_key, direction)

    def get_ordering(self):
        order_fields, order_key, direction = self.get_order_settings()
        ordering = order_fields[order_key]
        #if direction is 'desc' or is invalid use descending order
        if direction != 'asc':
            ordering = '-' + ordering
        #default ordering will be '-updated'
        return ordering

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order_fields, order_key, direction = self.get_order_settings()
        context['order'] = order_key
        context['direction'] = direction
        #get all but the last order key, which is 'default'
        context['order_fields'] = list(order_fields.keys())[:-1]
        return context
    
    
    def get_order_fields(self):
        """Return a dict mapping friendly names to field names and lookups."""
        return {
            'phrase': 'sentence',
            'category': 'category__category',
            'creator': 'user__username',
            'created': 'created', 
            'updated': 'updated',
            'default_key': 'updated',
        }
    
    def get_queryset(self):
        ordering = self.get_ordering()
        qs = Phrase.objects.all()
        print(self.kwargs)
        if 'q' in self.request.GET: #Filter by search query
            q = self.request.GET.get('q')
            print(self.request.GET)
            print(q)
            qs = qs.filter(Q(sentence__icontains=q) | Q(author__icontains=q))
        if 'slug' in self.kwargs: #filter by category or tag
            slug = self.kwargs['slug']
            if '/category' in self.request.path_info:
                qs = qs.filter(category__slug=slug)
            if '/tag' in self.request.path_info:
                qs = qs.filter(tags__slug=slug)
        elif 'username' in self.kwargs: #filter by Creator
            username = self.kwargs['username']
            qs = qs.filter(user__username=username)
        return qs.order_by(ordering)

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

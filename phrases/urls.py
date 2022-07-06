from django.urls import path
from .views import (PhraseListView, PhraseDetailView, PhraseCreateView, 
PhraseUpdateView, PhraseDeleteView, vote)

app_name = 'phrases'

urlpatterns = [
    path('', PhraseListView.as_view(), name='list'),
    path('phrase/create/', PhraseCreateView.as_view(), name='create'),
    path('phrase/<slug>/', PhraseDetailView.as_view(), name='detail'),
    path('phrase/<slug>/update/', PhraseUpdateView.as_view(), name='update'),
    path('phrase/<slug>/vote/', vote, name='ajax-vote'),
    path('phrase/<slug>/delete/', PhraseDeleteView.as_view(), name='delete'),
    path('category/<slug>/', PhraseListView.as_view(), name='category'),
    path('tag/<slug>/', PhraseListView.as_view(), name='tag'),
    path('creator/<username>/', PhraseListView.as_view(), name='creator'),

]
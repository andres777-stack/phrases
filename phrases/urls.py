from django.urls import path
from .views import (PhraseListView, PhraseDetailView, PhraseCreateView, 
PhraseUpdateView, PhraseDeleteView)

app_name = 'phrases'

urlpatterns = [
    path('', PhraseListView.as_view(), name='list'),
    path('joke/<int:pk>/', PhraseDetailView.as_view(), name='detail'),
    path('joke/create/', PhraseCreateView.as_view(), name='create'),
    path('joke/<int:pk>/update/', PhraseUpdateView.as_view(), name='update'),
    path('joke/<int:pk>/delete/', PhraseDeleteView.as_view(), name='delete'),

]
from django.urls import path
from .views import PhraseListView, PhraseDetailView

app_name = 'phrases'

urlpatterns = [
    path('', PhraseListView.as_view(), name='list'),
    path('joke/<int:pk>/', PhraseDetailView.as_view(), name='detail'),
]
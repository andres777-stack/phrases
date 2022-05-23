from django.urls import path
from .views import PhraseListView

app_name = 'phrases'

urlpatterns = [
    path('', PhraseListView.as_view(), name='list'),
]
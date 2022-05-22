from django.urls import path
from .views import TemplateView

app_name = 'phrases'

urlpatterns = [
    path('', TemplateView.as_view(), name='phrases'),
]
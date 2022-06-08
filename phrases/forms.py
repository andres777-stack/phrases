from django import forms
from django.forms import ModelForm, Textarea, CharField
from django import forms

from .models import Phrase

class PhraseForm(ModelForm):
    class Meta:
        model = Phrase
        fields = ['sentence', 'author', 'category', 'tags']

        widgets = {
            'sentence' : forms.Textarea(attrs={'cols': 80, 'rows': 3, 'autofocus': True}),
            'author' : forms.TextInput(attrs={'placeholder': "Write the author's name"}),
        }
        #Charfield trajo problemas con attrs.

        help_texts = {
            'sentence': 'Write a wise sentence.',
            'tags' : 'Use Ctrl-click to select multiple tags.'
        }
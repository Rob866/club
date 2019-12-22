from .models import Comentario
from django import forms
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'email', 'body')

from django import forms
from .models import Cmt

class CommentForm(forms.ModelForm):
    class Meta:
        model = Cmt
        fields = ['body']
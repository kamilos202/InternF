from django import forms
from .models import Post


class EchoForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('post',)

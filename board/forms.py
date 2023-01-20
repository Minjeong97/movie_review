from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(min_length=2, max_length=100)

    class Meta:
        model = Article
        fields = ('title', 'content',)
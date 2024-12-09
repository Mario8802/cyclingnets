from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    """
    Form for creating and editing news articles.
    """
    class Meta:
        model = News
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter content', 'rows': 5}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'News Title',
            'content': 'Content',
            'image': 'Image (optional)',
        }

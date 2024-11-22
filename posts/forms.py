from django import forms
from .models import BikePost
from .models import Post


class BikePostForm(forms.ModelForm):
    class Meta:
        model = BikePost
        fields = ['title', 'description', 'category']



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']

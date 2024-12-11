from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    """
    A Django ModelForm for creating and editing news articles.

    This form is tied to the News model and includes fields for:
    - title: The title of the news article.
    - content: The main content of the news article.
    - image: An optional image associated with the article.
    """

    class Meta:
        model = News  # Specify the model this form is based on
        fields = ['title', 'content', 'image']  # Fields to include in the form

        # Custom widgets for each field to enhance the form's appearance and usability
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',  # Add Bootstrap styling for consistency
                    'placeholder': 'Enter title'  # Placeholder text for user guidance
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',  # Add Bootstrap styling for larger input area
                    'placeholder': 'Enter content',  # Placeholder text for user guidance
                    'rows': 5  # Set height of the textarea
                }
            ),
            'image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'  # Add Bootstrap styling for file input
                }
            ),
        }

        # Custom labels for each field to make the form more user-friendly
        labels = {
            'title': 'News Title',  # Label for the title field
            'content': 'Content',  # Label for the content field
            'image': 'Image (optional)',  # Label for the image field
        }

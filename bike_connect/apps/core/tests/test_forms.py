from django.test import TestCase
from cyclingnets.bike_connect.apps.core.forms import NewsForm


class NewsFormTest(TestCase):
    """
    Tests for the NewsForm used for creating and editing news articles.
    """

    def test_news_form_valid_data(self):
        """
        Test if the form is valid when provided with correct data.
        """
        form = NewsForm(data={
            'title': 'Test News',
            'content': 'This is a test content.',
        })
        self.assertTrue(form.is_valid())

    def test_news_form_missing_title(self):
        """
        Test if the form is invalid when the 'title' field is missing or empty.
        """
        form = NewsForm(data={
            'title': '',
            'content': 'This is a test content.',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_news_form_widget_placeholders(self):
        """
        Test if the 'title' and 'content' fields have correct placeholders.
        """
        form = NewsForm()
        self.assertEqual(form.fields['title'].widget.attrs['placeholder'], 'Enter title')
        self.assertEqual(form.fields['content'].widget.attrs['placeholder'], 'Enter content')

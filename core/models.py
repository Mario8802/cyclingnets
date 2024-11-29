from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)  # Заглавие на новината
    content = models.TextField()  # Съдържание на новината
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)  # Изображение (опционално)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата на създаване
    updated_at = models.DateTimeField(auto_now=True)  # Последна промяна

    def __str__(self):
        return self.title


class Page(models.Model):
    title = models.CharField(max_length=200)  # Заглавие на страницата
    slug = models.SlugField(unique=True)  # Уникален slug за URL
    content = models.TextField()  # Съдържание на страницата
    created_at = models.DateTimeField(auto_now_add=True)  # Дата на създаване
    updated_at = models.DateTimeField(auto_now=True)  # Последна промяна

    def __str__(self):
        return self.title

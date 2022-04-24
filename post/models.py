from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    CHOICES = [
        ('follower', "follower"),
        ('all', 'all'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор поста')
    title = models.CharField(max_length=100, verbose_name='Заголовок поста')
    text = models.TextField(max_length=500, verbose_name='Текст поста')
    reader_role = models.CharField(max_length=10, choices=CHOICES, verbose_name='Роль читателя')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title

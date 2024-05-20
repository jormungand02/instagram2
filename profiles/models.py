from django.db import models
from django.contrib.auth import get_user_model

from posts.models import Post

User = get_user_model()

class Profile(models.Model):
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural  = 'Профили'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='email')
    avatar = models.ImageField(upload_to='avatars/', blank=True, verbose_name='Аватарка')
    bio = models.TextField(blank=True, verbose_name='О себе')
    location = models.CharField(max_length=100, blank=True, verbose_name='Местоположение')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')

    def __str__(self):
        return f'Профиль {self.user}'


class SavedPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_posts', verbose_name='Пользователь')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='saved_by', verbose_name='Пост')

    class Meta:
        unique_together = ('user', 'post')
        verbose_name = 'Сохраненный пост'
        verbose_name_plural  = 'Сохраненные посты'

    def __str__(self):
        return f'{self.user} сохраненный пост {self.post.title}'

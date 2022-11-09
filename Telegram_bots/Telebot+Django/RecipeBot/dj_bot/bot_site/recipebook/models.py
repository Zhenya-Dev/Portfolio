from django.db import models


class RecipeBook(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ім\'я')
    last_name = models.CharField(max_length=255, verbose_name='Прізвище')
    user_name = models.CharField(max_length=255, verbose_name='username')
    user_id = models.IntegerField(verbose_name='User Id')
    profile_name = models.CharField(
        max_length=255, verbose_name='Ім\'я з анкети')
    gender = models.CharField(max_length=255, verbose_name='Стать')

    class Meta:
        verbose_name = 'Список користувачів'
        verbose_name_plural = 'Список користувачів'
        ordering = [
            'name',
            'last_name',
            'user_name',
            'user_id',
            'profile_name',
            'gender']


class RecipeBook_recipe(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назва')
    photo = models.ImageField(upload_to='photo', verbose_name='Фото')
    description = models.TextField(blank=True, verbose_name='Опис')

    class Meta:
        verbose_name = 'Список страв'
        verbose_name_plural = 'Список страв'
        ordering = ['id', 'title', 'description']


class FSM(models.Model):
    fsm_flag = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'FSM_readonly'
        verbose_name_plural = 'FSM_readonly'

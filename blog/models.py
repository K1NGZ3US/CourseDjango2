from django.db import models


class Category(models.Model):
    """Category model"""
    name = models.CharField("Имя", max_length=100)
    slug = models.SlugField("url", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tag(models.Model):
    """Tag model"""
    name = models.CharField("Тег", max_length=50)
    slug = models.SlugField("url", max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
    

class Post(models.Model):
    """Post model"""
    title = models.CharField("Название", max_length=100)
    mini_text = models.TextField("Поле мини-текста")
    text = models.TextField("Поле текста")
    created_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField("url", max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

class Comment(models.Model):
    """Comment model"""
    text = models.TextField("Текст комментария")
    created_date = models.DateTimeField(auto_now_add=True)
    moderation = models.BooleanField()
    
    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
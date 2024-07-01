from django.db import models


# Create your models here.

class Users(models.Model):
    Username = models.CharField(max_length=50)
    Name = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Email = models.EmailField(unique=True)
    Age = models.IntegerField()

    def __str__(self):
        return self.Name


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='group11/templates/articles/picture/', null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author_name} on {self.article}'


class Notes(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='notes')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

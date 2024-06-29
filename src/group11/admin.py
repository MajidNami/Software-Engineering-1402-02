from django.contrib import admin
from .models import Author, Category, Notes, Article, Comment

# Register your models here.


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Notes)



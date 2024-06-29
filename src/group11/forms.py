from django import forms
from .models import Author, Category, Article, Comment, Notes


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio', 'email']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'author', 'category', 'picture']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'content']


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'user', 'content']
from django.urls import path
from .views import (
    HomepageView,
    AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView,
    CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    CategoryArticlesView,
    ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView,
    CommentCreateView, CommentListView, CommentDeleteView,
    NotesListView, NotesDetailView, NotesCreateView, NotesUpdateView, NotesDeleteView
)

urlpatterns = [
    path('', HomepageView, name='homepage'),

    path('authors/', AuthorListView, name='author_list'),
    path('authors/<int:pk>/', AuthorDetailView, name='author_detail'),
    path('authors/new/', AuthorCreateView, name='author_create'),
    path('authors/<int:pk>/edit/', AuthorUpdateView, name='author_update'),
    path('authors/<int:pk>/delete/', AuthorDeleteView, name='author_delete'),

    path('categories/', CategoryListView, name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView, name='category_detail'),
    path('categories/new/', CategoryCreateView, name='category_create'),
    path('categories/<int:pk>/edit/', CategoryUpdateView, name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView, name='category_delete'),
    path('categories/<int:category_id>/show', CategoryArticlesView, name='category_articles'),


    path('articles/', ArticleListView, name='article_list'),
    path('articles/<int:pk>/', ArticleDetailView, name='article_detail'),
    path('articles/new/', ArticleCreateView, name='article_create'),
    path('articles/<int:pk>/edit/', ArticleUpdateView, name='article_update'),
    path('articles/<int:pk>/delete/', ArticleDeleteView, name='article_delete'),

    path('articles/<int:article_id>/comments/', CommentListView, name='comment_list'),
    path('articles/<int:article_id>/comments/new/', CommentCreateView, name='comment_create'),

    path('notes/', NotesListView, name='note_list'),
    path('notes/<int:pk>/', NotesDetailView, name='note_detail'),
    path('notes/new/', NotesCreateView, name='note_create'),
    path('notes/<int:pk>/edit/', NotesUpdateView, name='note_update'),
    path('notes/<int:pk>/delete/', NotesDeleteView, name='note_delete'),
]


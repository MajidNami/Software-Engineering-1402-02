from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Author, Category, Article, Comment, Notes
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import AuthorForm, CategoryForm, ArticleForm, CommentForm, NotesForm


# Create your views here.
def HomepageView(request):
    categories = Category.objects.all()
    articles = Article.objects.all()
    context = {
        'categories': categories,
        'articles': articles,
    }
    return render(request, 'homepage.html', context)


def AuthorListView(request):
    authors = Author.objects.all()  # Retrieve all authors
    return render(request, 'author/author_list.html', {'authors': authors})


def AuthorDetailView(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author/author_detail.html', {'author': author})


def AuthorCreateView(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'author/author_form.html', {'form': form})


def AuthorUpdateView(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_detail', pk=author.pk)
    else:
        form = AuthorForm(instance=author)
    return render(request, 'author/author_form.html', {'form': form})


def AuthorDeleteView(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'author/author_confirm_delete.html', {'author': author})


def CategoryListView(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})


def CategoryDetailView(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category/category_detail.html', {'category': category})


def CategoryCreateView(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category/category_form.html', {'form': form})


def CategoryUpdateView(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category/category_form.html', {'form': form})


def CategoryDeleteView(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category/category_confirm_delete.html', {'category': category})


def ArticleListView(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})


def ArticleDetailView(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/article_detail.html', {'article': article})


def ArticleCreateView(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'articles/article_form.html', {'form': form})


def ArticleUpdateView(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/article_form.html', {'form': form})


def ArticleDeleteView(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'articles/article_confirm_delete.html', {'article': article})


def CommentListView(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comments.all()  # Using the related_name 'comments' to access related Comment objects
    return render(request, 'comments/comment_list.html', {'article': article, 'comments': comments})


def CommentCreateView(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = CommentForm()
    return render(request, 'comments/comment_form.html', {'form': form, 'article': article})


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'newspaper/comment_confirm_delete.html'
    success_url = reverse_lazy('article_list')


def NotesListView(request):
    notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': notes})


def NotesDetailView(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    return render(request, 'notes/notes_detail.html', {'note': note})


def NotesCreateView(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes_list')
    else:
        form = NotesForm()
    return render(request, 'notes/notes_form.html', {'form': form})


def NotesUpdateView(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes_detail', pk=note.pk)
    else:
        form = NotesForm(instance=note)
    return render(request, 'notes/notes_form.html', {'form': form})


def NotesDeleteView(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    note.delete()
    return redirect('notes_list')

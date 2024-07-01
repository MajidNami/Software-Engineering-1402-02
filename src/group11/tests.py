from .models import Article, Comment, Notes
from datetime import timezone
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from .forms import AuthorForm

from models import Author
from .models import Category


class AuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 3 authors for test
        Author.objects.create(name='Author 1', bio='Bio 1', email='ali1@gmail.com')
        Author.objects.create(name='Author 2', bio='Bio 2', email='ali2@gmail.com')
        Author.objects.create(name='Author 3', bio='Bio 3', email='ali3@gmail.com')

    def test_view_url_exists_at_desired_location(self):
        author_list_url = reverse('author_list')
        # response = self.client.get('authors/')
        # self.assertEqual(response.status_code, 200)
        print("the author list url", author_list_url)

    def test_view_accessible_by_name(self):
        response = self.client.get(reverse('author_list'))
        self.assertEqual(response.status_code, 200)
        print("done1")

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('author_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author/author_list.html')
        print("done2")

    def test_view_lists_all_authors(self):
        response = self.client.get(reverse('author_list'))
        self.assertEqual(response.status_code, 200)
        # self.assertTrue(len(response.context['authors']) == 3)
        print("done3")


#/////////////////////////////////////////////
class AuthorDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create an author for testing
        cls.author = Author.objects.create(
            name='Test Author',
            bio='This is a test bio',
            email='testauthor@example.com'
        )

    def test_view_url_exists_at_desired_location(self):
        # Test the URL for the AuthorDetailView exists and returns a 200 status code
        response = self.client.get(f'author/{self.author.pk}/')
        self.assertEqual(response.status_code, 200)
        print("Detail-1 Done")

    def test_view_accessible_by_name(self):
        # Test the URL named 'author_detail' for the AuthorDetailView is accessible
        #response = self.client.get(reverse('author_detail'))
        response = self.client.get(reverse('author_detail', args=[self.author.pk]))
        self.assertEqual(response.status_code, 200)

    def test_view_context_contains_author(self):
        # Test that the context contains the correct author
        response = self.client.get(reverse('Alishafa', args=[self.author.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['author'], self.author)
        print("Detail-3 Done")

    def test_view_404_for_invalid_author(self):
        # Test that a 404 is returned for a non-existent author
        response = self.client.get(reverse('author_detail', args=[999]))
        self.assertEqual(response.status_code, 404)
        print("Detail-4 Done")


#/////////////////////////////////////////////////


class AuthorCreateViewTests(TestCase):
    def test_view_url_exists_at_desired_location(self):
        # بررسی اینکه آیا URL به درستی کار می‌کند
        response = self.client.get('/authors/create/')
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        # بررسی اینکه آیا URL با استفاده از نام آن به درستی کار می‌کند
        response = self.client.get(reverse('author_create'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        # بررسی اینکه آیا نمای از قالب درست استفاده می‌کند
        response = self.client.get(reverse('author_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author/author_form.html')

    def test_view_contains_form(self):
        # بررسی اینکه آیا نمای فرم را شامل می‌شود
        response = self.client.get(reverse('author_create'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], AuthorForm)

    def test_post_creates_author(self):
        # بررسی اینکه آیا ارسال فرم یک نویسنده جدید ایجاد می‌کند
        data = {
            'name': 'New Author',
            'bio': 'This is a new author.',
            'email': 'example@gmail.com'
        }
        response = self.client.post(reverse('author_create'), data)
        self.assertEqual(response.status_code, 302)  # بررسی اینکه آیا به درستی ریدایرکت می‌شود
        self.assertEqual(Author.objects.count(), 1)  # بررسی اینکه آیا یک نویسنده جدید ایجاد شده است
        self.assertEqual(Author.objects.first().name, 'New Author')  # بررسی نام نویسنده ایجاد شده

    def test_invalid_post_does_not_create_author(self):
        # بررسی اینکه آیا ارسال فرم نامعتبر یک نویسنده جدید ایجاد نمی‌کند
        data = {
            'name': '',  # نام خالی که نامعتبر است
            'bio': 'This is an invalid author.',
            'email': 'example@gmail.com'
        }
        response = self.client.post(reverse('author_create'), data)
        self.assertEqual(response.status_code, 200)  # باید به صفحه فرم بازگردد
        self.assertEqual(Author.objects.count(), 0)  # نباید هیچ نویسنده‌ای ایجاد شود


#//////////////////////////////


class AuthorUpdateViewTests(TestCase):
    def setUp(self):
        # ایجاد یک نویسنده برای استفاده در آزمون‌ها
        self.author = Author.objects.create(name='Existing Author', bio='Existing bio.', email='ex@gmail.com',
                                            created_at=timezone.now())

    def test_view_url_exists_at_desired_location(self):
        # بررسی اینکه آیا URL به درستی کار می‌کند
        response = self.client.get(f'/authors/{self.author.pk}/update/')
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        # بررسی اینکه آیا URL با استفاده از نام آن به درستی کار می‌کند
        response = self.client.get(reverse('author_update', args=[self.author.pk]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        # بررسی اینکه آیا نمای از قالب درست استفاده می‌کند
        response = self.client.get(reverse('author_update', args=[self.author.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author/author_form.html')

    def test_view_contains_form_with_instance(self):
        # بررسی اینکه آیا نمای فرم را با نویسنده موجود شامل می‌شود
        response = self.client.get(reverse('author_update', args=[self.author.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], AuthorForm)
        self.assertEqual(response.context['form'].instance, self.author)

    def test_post_updates_author(self):
        # بررسی اینکه آیا ارسال فرم نویسنده را به‌روزرسانی می‌کند
        data = {
            'name': 'Updated Author',
            'bio': 'This is an updated author.',
            'email': 'ex@gmail.com'
        }
        response = self.client.post(reverse('author_update', args=[self.author.pk]), data)
        self.assertEqual(response.status_code, 302)  # بررسی اینکه آیا به درستی ریدایرکت می‌شود
        self.author.refresh_from_db()
        self.assertEqual(self.author.name, 'Updated Author')  # بررسی نام به‌روزرسانی شده نویسنده
        self.assertEqual(self.author.bio, 'This is an updated author.')  # بررسی بیوگرافی به‌روزرسانی شده نویسنده

    def test_invalid_post_does_not_update_author(self):
        # بررسی اینکه آیا ارسال فرم نامعتبر نویسنده را به‌روزرسانی نمی‌کند
        data = {
            'name': '',  # نام خالی که نامعتبر است
            'bio': 'This is an invalid update.',
            'email': 'ex@gmail.com'
        }
        response = self.client.post(reverse('author_update', args=[self.author.pk]), data)
        self.assertEqual(response.status_code, 200)  # باید به صفحه فرم بازگردد
        self.author.refresh_from_db()
        self.assertNotEqual(self.author.bio, 'This is an invalid update.')  # نباید بیوگرافی به‌روزرسانی شود

    def test_view_404_for_invalid_author(self):
        # بررسی اینکه آیا درخواست برای نویسنده غیرموجود منجر به بازگشت وضعیت 404 می‌شود
        response = self.client.get(reverse('author_update', args=[9999]))  # شناسه نامعتبر
        self.assertEqual(response.status_code, 404)


#///////////////////


class AuthorDeleteViewTests(TestCase):
    def setUp(self):
        # ایجاد یک نویسنده برای استفاده در آزمون‌ها
        self.author = Author.objects.create(name='Existing Author', bio='Existing bio.', email='auth@gmail.com',
                                            created_at=timezone.now())

    def test_view_url_exists_at_desired_location(self):
        # بررسی اینکه آیا URL به درستی کار می‌کند
        response = self.client.get(f'/authors/{self.author.pk}/delete/')
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        # بررسی اینکه آیا URL با استفاده از نام آن به درستی کار می‌کند
        response = self.client.get(reverse('author_delete', args=[self.author.pk]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        # بررسی اینکه آیا نمای از قالب درست استفاده می‌کند
        response = self.client.get(reverse('author_delete', args=[self.author.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author/author_confirm_delete.html')

    def test_view_contains_author(self):
        # بررسی اینکه آیا نمای شامل نویسنده است
        response = self.client.get(reverse('author_delete', args=[self.author.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['author'], self.author)

    def test_post_deletes_author(self):
        # بررسی اینکه آیا ارسال درخواست POST نویسنده را حذف می‌کند
        response = self.client.post(reverse('author_delete', args=[self.author.pk]))
        self.assertEqual(response.status_code, 302)  # بررسی اینکه آیا به درستی ریدایرکت می‌شود
        self.assertEqual(Author.objects.count(), 0)  # بررسی اینکه آیا نویسنده حذف شده است

    def test_invalid_author_returns_404(self):
        # بررسی اینکه آیا درخواست برای نویسنده غیرموجود منجر به بازگشت وضعیت 404 می‌شود
        response = self.client.get(reverse('author_delete', args=[9999]))  # شناسه نامعتبر
        self.assertEqual(response.status_code, 404)


#/////////////////////////////////////////////////
# # this is one is working
class CategoryListViewTests(TestCase):
    def setUp(self):
        # ایجاد چند دسته‌بندی برای آزمون
        # self.category1 = Category.objects.create(name='Category 1', created_at=timezone.now())
        # self.category2 = Category.objects.create(name='Category 2', created_at=timezone.now())
        self.category1 = Category.objects.create(name='Category 1')
        self.category2 = Category.objects.create(name='Category 2')

    def test_view_url_exists_at_desired_location(self):
        # بررسی اینکه آیا URL به درستی کار می‌کند
        response = self.client.get('categories/')
        self.assertEqual(response.status_code, 200)
        print("D1")

    def test_view_accessible_by_name(self):
        # بررسی اینکه آیا URL با استفاده از نام آن به درستی کار می‌کند
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        print("D2")

    def test_view_uses_correct_template(self):
        # بررسی اینکه آیا نمای از قالب درست استفاده می‌کند
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category/category_list.html')
        print("D3")

    def test_view_returns_all_categories(self):
        # بررسی اینکه آیا همه دسته‌بندی‌ها به قالب ارسال می‌شوند
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        # self.assertQuerysetEqual(response.context['categories'],
        #     [repr(self.category1), repr(self.category2)],
        #     ordered=False
        # )
        print("D4")


#//////////////////////////////////////////////
#

class CategoryDetailViewTests(TestCase):
    def setUp(self):
        # ایجاد چند دسته‌بندی برای آزمون
        self.category1 = Category.objects.create(name='Category 1')
        self.category2 = Category.objects.create(name='Category 2')
        # self.category1 = Category.objects.create(name='Category 1', created_at=timezone.now())
        # self.category2 = Category.objects.create(name='Category 2', created_at=timezone.now())

        print("D1")

    def test_view_url_exists_at_desired_location(self):
        # بررسی اینکه آیا URL به درستی کار می‌کند
        response = self.client.get(f'/categories/{self.category1.pk}/')
        self.assertEqual(response.status_code, 200)
        print("D2")

    def test_view_accessible_by_name(self):
        # بررسی اینکه آیا URL با استفاده از نام آن به درستی کار می‌کند
        response = self.client.get(reverse('category_detail', args=[self.category1.pk]))
        self.assertEqual(response.status_code, 200)
        print("D3")

    def test_view_uses_correct_template(self):
        # بررسی اینکه آیا نمای از قالب درست استفاده می‌کند
        response = self.client.get(reverse('category_detail', args=[self.category1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category/category_detail.html')
        print("D4")

    def test_view_returns_correct_category(self):
        # بررسی اینکه آیا دسته‌بندی صحیح به قالب ارسال می‌شود
        response = self.client.get(reverse('category_detail', args=[self.category1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['category'], self.category1)
        print("D5")

    def test_view_404_for_invalid_category(self):
        # بررسی اینکه آیا درخواست برای دسته‌بندی غیرموجود منجر به بازگشت وضعیت 404 می‌شود
        response = self.client.get(reverse('category_detail', args=[9999]))  # شناسه نامعتبر
        self.assertEqual(response.status_code, 404)
        print("D6")


class CategoryViewsTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def test_category_create_view(self):
        response = self.client.get(reverse('category_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category/category_form.html')

        data = {'name': 'New Category'}
        response = self.client.post(reverse('category_create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Category.objects.count(), 2)

    def test_category_update_view(self):
        response = self.client.get(reverse('category_update', args=[self.category.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category/category_form.html')

        data = {'name': 'Updated Category'}
        response = self.client.post(reverse('category_update', args=[self.category.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, 'Updated Category')

    def test_category_delete_view(self):
        response = self.client.get(reverse('category_delete', args=[self.category.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category/category_confirm_delete.html')

        response = self.client.post(reverse('category_delete', args=[self.category.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Category.objects.count(), 0)

    def test_category_articles_view(self):
        article = Article.objects.create(title='Test Article', content='Test Content', category=self.category)
        response = self.client.get(reverse('category_articles', args=[self.category.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category/category_articles.html')
        self.assertIn(article, response.context['articles'])


class ArticleViewsTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.article = Article.objects.create(title='Test Article', content='Test Content', category=self.category)

    def test_article_list_view(self):
        response = self.client.get(reverse('article_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_list.html')
        self.assertIn(self.article, response.context['articles'])

    def test_article_detail_view(self):
        response = self.client.get(reverse('article_detail', args=[self.article.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_detail.html')
        self.assertEqual(response.context['article'], self.article)

    def test_article_create_view(self):
        response = self.client.get(reverse('article_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_form.html')

        data = {'title': 'New Article', 'content': 'New Content', 'category': self.category.pk}
        response = self.client.post(reverse('article_create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Article.objects.count(), 2)

    def test_article_update_view(self):
        response = self.client.get(reverse('article_update', args=[self.article.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_form.html')

        data = {'title': 'Updated Article', 'content': 'Updated Content', 'category': self.category.pk}
        response = self.client.post(reverse('article_update', args=[self.article.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.article.refresh_from_db()
        self.assertEqual(self.article.title, 'Updated Article')

    def test_article_delete_view(self):
        response = self.client.get(reverse('article_delete', args=[self.article.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_confirm_delete.html')

        response = self.client.post(reverse('article_delete', args=[self.article.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Article.objects.count(), 0)


class CommentViewsTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.article = Article.objects.create(title='Test Article', content='Test Content', category=self.category)
        self.comment = Comment.objects.create(article=self.article, text='Test Comment')

    def test_comment_list_view(self):
        response = self.client.get(reverse('comment_list', args=[self.article.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'comments/comment_list.html')
        self.assertIn(self.comment, response.context['comments'])

    def test_comment_create_view(self):
        response = self.client.get(reverse('comment_create', args=[self.article.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'comments/comment_form.html')

        data = {'text': 'New Comment'}
        response = self.client.post(reverse('comment_create', args=[self.article.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.count(), 2)

    # def test_comment_delete_view(self):
    #     response = self.client.get(reverse('comment_delete', args=[self.comment.pk]))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'comments/comment_confirm_delete.html')
    #
    #     response = self.client.post(reverse('comment_delete', args=[self.comment.pk]))
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(Comment.objects.count(), 0)


class NotesViewsTests(TestCase):
    def setUp(self):
        self.note = Notes.objects.create(title='Test Note', content='Test Content', created_at=timezone.now())

    def test_notes_list_view(self):
        response = self.client.get(reverse('notes_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/notes_list.html')
        self.assertIn(self.note, response.context['notes'])

    def test_notes_detail_view(self):
        response = self.client.get(reverse('notes_detail', args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/notes_detail.html')
        self.assertEqual(response.context['note'], self.note)

    def test_notes_create_view(self):
        response = self.client.get(reverse('notes_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/notes_form.html')

        data = {'title': 'New Note', 'content': 'New Content'}
        response = self.client.post(reverse('notes_create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Notes.objects.count(), 2)

    def test_notes_update_view(self):
        response = self.client.get(reverse('notes_update', args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/notes_form.html')

        data = {'title': 'Updated Note', 'content': 'Updated Content'}
        response = self.client.post(reverse('notes_update', args=[self.note.pk]), data)
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')

    def test_notes_delete_view(self):
        response = self.client.get(reverse('notes_delete', args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_confirm_delete.html')

        response = self.client.post(reverse('notes_delete', args=[self.note.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Notes.objects.count(), 0)

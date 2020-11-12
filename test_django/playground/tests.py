from datetime import date

from django.test import TestCase

from .models import Article, Publisher


class ArticleTestCase(TestCase):
    recently_added_article = 'recently_added_article'
    old_article = 'old_article'

    def setUp(self) -> None:
        publisher = Publisher.objects.create(
            first_name='John',
            last_name='Smith',
            email='john@smith.com',
        )

        Article.objects.create(
            title=self.recently_added_article,
            pub_date=date.today(),
            publisher=publisher,
        )

        Article.objects.create(
            title=self.old_article,
            pub_date=date(2018, 1, 13),
            publisher=publisher,
        )

    def test_added_recently_true(self):
        article = Article.objects.get(title=self.recently_added_article)
        self.assertTrue(article.added_recently)

    def test_added_recently_false(self):
        article = Article.objects.get(title=self.old_article)
        self.assertFalse(article.added_recently)


class AnotherTestCase(TestCase):

    def test_always_fail(self):
        self.assertTrue(True)


class PlaygroundViewTestCase(TestCase):

    def setUp(self) -> None:
        publisher = Publisher.objects.create(
            first_name='John',
            last_name='Smith',
            email='john@smith.com',
        )

        for title in map(str, range(100)):
            Article.objects.create(
                title=title,
                pub_date=date.today(),
                publisher=publisher,
            )

    def test_index(self):
        response = self.client.get('/playground/')
        articles = [a for a in response.context['articles']]
        expected_articles = [a for a in Article.objects.all()]
        self.assertEqual(articles, expected_articles)

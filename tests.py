from django.test import TestCase
from .models import ArticleModel
from datetime import datetime, timezone

# Create your tests here.
class ArticleTest(TestCase):
    def test_article_created_success(self):
        ArticleModel.objects.create(title="test article", category="test category", author="test admin", content="test content", created_at=datetime.now(timezone.utc))
        article = ArticleModel.objects.get(title="test article")
        self.assertEqual(article.category, "test category")

class HomepageTest(TestCase):
    def test_home_content(self):
        response = self.client.get("/wellbeing/")  # Adjust the URL to match your homepage URL
        self.assertEqual(response.status_code, 200)  # Check if the response status is OK
        self.assertContains(response, "welcome to your safe space", status_code=200)


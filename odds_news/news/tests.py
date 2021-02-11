from django.test import TestCase

from .models import News
from categories.models import Category


class TestNewsView(TestCase):
    def test_view_should_see_title_and_category_name_and_content(self):
        # Given
        category = Category.objects.create(name='Data Science')
        News.objects.create(title='ODDS', content='Hello', category=category)

        # When
        response = self.client.get('/news1/')

        # Then
        assert 'ODDS' in str(response.content)
        assert 'Data Science' in str(response.content)
        assert 'Hello' in str(response.content)
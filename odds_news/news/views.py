import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from news.models import News


class NewsAPIView(View):
    def get(self, request):
        news = News.objects.all()

        data = []
        for each in news:
            item = {
                'title': each.title,
                'content': each.content,
                'category': each.category.name,
            }
            data.append(item)

        return HttpResponse(
            json.dumps(data),
            content_type='application/json'
        )


class NewsView(View):
    def get(self, request):
        news = News.objects.all()
        return render(
            request,
            'news.html',
            {
                'news': news
            }
        )


def news_view(request):
    if request.method == 'GET':
        news = News.objects.all()
        html = '<div>'
        for each in news:
            html += '<div>'
            html += f'<h1>{each.title}</h1>'
            html += f'<p>{each.content}</p>'
            html += '</div>'
        html += '</div>'
        return HttpResponse(html)
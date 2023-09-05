from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound
from django.views import View
from datetime import datetime
from .models import ArticleModel
from django.utils import timezone
# Create your views here.

from django.shortcuts import render
from django.views import View

class Home(View):
    def get(self, request):
        return render(request, 'home.html', {'message': 'welcome to your safe space'})

# pls change to something related to wellbeing
class Article(View):
    def get(self, request):
        articles = ArticleModel.objects.all()
        return render(request, 'article.html', {'articles': articles})
    
    def post(self, request):
        title = request.POST['title']
        category = request.POST['category']
        author = request.POST['author']
        content = request.POST['content']

        article = ArticleModel(title=title, category=category, author=author, content=content, created_at=datetime.now(tz=timezone.utc))

        article.save()
        
        # Redirect to a success page or the article list page
        return redirect('article')  # Replace with the appropriate URL name
#article details class   
class Details(View):
    def get(self,request,id):
        try:
            article = ArticleModel.objects.get(id=id)
            return render(request, "Details.html",{'article':article})
        except ArticleModel.DoesNotExist:
            return HttpResponseNotFound()
        
from django.urls import path
from .views import Article,Details

urlpatterns = [
    path('article/', Article.as_view(),name='article'),
      path("article/<int:id>",Details.as_view()),  # No need for 'wellbeing/article/'
]

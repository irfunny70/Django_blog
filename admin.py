from django.contrib import admin
from .models import ArticleModel
# Register your models here.
#use admin decorator
@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author","created_at")
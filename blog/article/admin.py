from django.contrib import admin

from .models import Article

# Register your models here.

#admin paneli özelliştirmeleri


@admin.register(Article)

class ArticleAdmin(admin.ModelAdmin):

    list_display=["baslik","yazar","olusturma_tarihi"] 
    search_fields=["baslik"]
    class Meta:
        model = Article



from django.contrib import admin
from articles.models import Article



class ArticleAdmin(admin.ModelAdmin):
    # Set Sequence of field in Admin Panel
    fields = ['title', 'image', 'description', 'year', 'slug']
    # Use for slug that upon Title
    prepopulated_fields = {"slug": ("title",)}
    # Display in Admin
    list_display = ('title', 'created', 'year')


admin.site.register(Article, ArticleAdmin)

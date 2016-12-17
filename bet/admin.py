from django.contrib import admin
from forms import ArticleAdminForm
from .models import Article,Block,Newsletter,Prognostika


def make_published(modeladmin, request, queryset):
    queryset.update(status='published')
make_published.short_description = "Mark selected stories as published"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created']
    list_filter = ['title','updated','tags']
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    actions = [make_published]
    form = ArticleAdminForm

class BlockAdmin(admin.ModelAdmin):
    list_display = ['title','status']

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['newsemail']

class PrognostikaAdmin(admin.ModelAdmin):
    list_display = ['kodikos','date']
    search_fields = ('date',)
    list_filter = ['date']

admin.site.register(Article,ArticleAdmin)
admin.site.register(Block,BlockAdmin)
admin.site.register(Newsletter,NewsletterAdmin)
admin.site.register(Prognostika,PrognostikaAdmin)

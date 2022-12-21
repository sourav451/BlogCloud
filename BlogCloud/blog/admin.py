from django.contrib import admin

from.models import Category,Blog

class BlogAdmin(admin.ModelAdmin):
    list_display=('title','published_at','publish')
    search_fields=('title','description')
    
    #to make the publish field editable
    list_editable=('publish',)
    ordering=('-id',)

admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
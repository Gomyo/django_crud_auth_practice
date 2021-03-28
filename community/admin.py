from django.contrib import admin
from .models import Review, Comment

# Register your models here.
class ReviewAdmin(models.ModelAdmin):
    list_display = ('pk', 'title', 'movie_title', 'rank', 'content', 'created_at', 'updated_at',)

class CommentAdmin(models.ModelAdmin):
    list_display = ('pk', 'content', 'created_at', 'updated_at',)

admin.site.register(Review, ReviewAdmin, Comment, CommentAdmin)

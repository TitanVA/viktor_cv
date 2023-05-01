from django.contrib import admin

from posts.models import Category, Summary, Jobs, Comment


class SummaryAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "author", "created_date")


class JobsAdmin(admin.ModelAdmin):
    list_display = ("company", "position", "author")


admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Summary, SummaryAdmin)
admin.site.register(Jobs, JobsAdmin)

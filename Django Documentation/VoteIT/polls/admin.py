from django.contrib import admin

from .models import Question, Choice

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question Information", {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["publication_date"]}),
    ]

    list_display = ["question_text", "publication_date", "was_published_recently"]

    inlines = [ChoiceInline]
    list_filter = ["publication_date"]
    search_fields = ['question_text']
admin.site.register(Question, QuestionAdmin)
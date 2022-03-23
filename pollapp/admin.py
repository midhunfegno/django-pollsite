from django.contrib import admin

# Register your models here.

from .models import Question, Choice

admin.site.register(Choice)


class ChoiceInline(admin.StackedInline):
    model = Choice
    fields = ('choice_text', )
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline, ]


admin.site.register(Question, QuestionAdmin)

from django.contrib import admin

from .models import Question, Choice

# admin.site.register(Question)
# Lame, default approach

# More control
class QuestionAdminSimple(admin.ModelAdmin):
    # Not using this, but this is a good simple way of doing things.
    fields = ['pub_date', 'question_text']


class ChoiceInline(admin.TabularInline): # StackedInLine makes it weird to read things
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # A bit more detailed, with the fields spread out some more.
    # Also featuring the classes.
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

# Overly simple, default way.
# admin.site.register(Choice)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['question_text']}),
        ('Informação da Data', {'fields': ['pub_date']}),
    ]
#admin.site.register(Question, QuestionAdmin)

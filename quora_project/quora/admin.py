from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Question,Answer,Like


class QuestionAdmin(admin.ModelAdmin):
    list_display =['title']
admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Answer, AnswerAdmin)

class LikeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Like, LikeAdmin)

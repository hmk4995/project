
from django.contrib import admin

# Register your models here.

from .models import Question, Contest, User, Candidate, Submission

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_id','question_name')

class ContestAdmin(admin.ModelAdmin):
    list_display = ('contest_name','questions')

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name','admin_privilege')

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('user_id','first_name')

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('language','time','score')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Contest, ContestAdmin)
admin.site.register(User, UserAdmin)
#admin.site.register(Test_case)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Submission, SubmissionAdmin)
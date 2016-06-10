
from django.contrib import admin

# Register your models here.

from .models import Question, Contest, Candidate, Submission,Test_case

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_id','question_name']
    search_fields = ['question_id','question_name']
    list_display_links = ['question_id','question_name']
    class Meta:
    	model = Question
    	ordering = ['question_id']

class ContestAdmin(admin.ModelAdmin):
    list_display = ['contest_name']
    search_fields = ['contest_name']
    #add date field
 
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('user_id','first_name')

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('language','time','score')

class Test_caseAdmin(admin.ModelAdmin):
    list_display = ('qno','sl_no')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Contest, ContestAdmin)
admin.site.register(Test_case,Test_caseAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Submission, SubmissionAdmin)
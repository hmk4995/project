
from django.contrib import admin

# Register your models here.

from .models import Question, Contest, Candidate, Submission,Test_case

class Test_caseInline(admin.TabularInline):
    model = Test_case
    ordering = ['sl_no']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        Test_caseInline,
    ]
    list_display = ['question_id','question_name']
    search_fields = ['question_id','question_name']
    list_display_links = ['question_id','question_name']
    class Meta:
    	model = Question
    	ordering = ['question_id']
    def delete_model(self,request, obj):
        delquestion=Test_case.objects.filter(qno=obj)
        delquestion.delete()
        super(ContestAdmin, self).delete_model(request, obj)    
 

class ContestAdmin(admin.ModelAdmin):
    list_display = ['contest_name']
    search_fields = ['contest_name']
    def save_model(self, request, obj, form, change):
        if change is False:
            for i in range(1,obj.no_of_candidates+1):
                i=Candidate.objects.get_or_create(contest=obj,user_name=obj.contest_name[:3]+"{0:03}".format(i),password=obj.contest_name[:3]+"pass"+"{0:03}".format(i))
            super(ContestAdmin, self).save_model(request, obj, form, change)
        else:
            print(obj.contest_name)
            print(get_changeform_initial_data)
            super(ContestAdmin, self).save_model(request, obj, form, change)
            # for i in range(1,obj.no_of_candidates+1):
            #     i=Candidate.objects.get_or_create(contest=obj,user_name=obj.contest_name[:3]+"{0:03}".format(i),password=obj.contest_name[:3]+"pass"+"{0:03}".format(i))

    # def get_changeform_initial_data(self, request):

    def delete_model(self,request, obj):
        delcandidate=Candidate.objects.filter(contest=obj)
        delcandidate.delete()
        super(ContestAdmin, self).delete_model(request, obj)    
 
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('user_name','first_name')

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('language','time','score')


class Test_caseAdmin(admin.ModelAdmin):
    list_display = ('qno','sl_no')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Contest, ContestAdmin)
admin.site.register(Test_case,Test_caseAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Submission, SubmissionAdmin)
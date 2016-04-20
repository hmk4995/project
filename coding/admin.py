
from django.contrib import admin

# Register your models here.

from .models import Question, Contest, User, Test_case, Candidate, Submission

admin.site.register(Question)
admin.site.register(Contest)
admin.site.register(User)
admin.site.register(Test_case)
admin.site.register(Candidate)
admin.site.register(Submission)
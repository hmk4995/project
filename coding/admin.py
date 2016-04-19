from django.contrib import admin

# Register your models here.from django.contrib import admin

from .models import Question, Contest, User, Test_case

admin.site.register(Question)
admin.site.register(Contest)
admin.site.register(User)
admin.site.register(Test_case)
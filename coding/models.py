

# Create your models here.
from django.db import models


class Contest(models.Model):
	contest_name = models.CharField(max_length=200)
	college_name = models.CharField(max_length=200)
	no_of_candidates = models.IntegerField(default=0)
	no_of_questions = models.IntegerField(default=0)
	def __str__(self):
		return self.contest_name 

class User(models.Model):
	contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
	user_name = models.CharField(max_length=200)
	def __str__(self):
		return self.user_name 

class Question(models.Model):
	contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
	question_name = models.CharField(max_length=200)
	def __str__(self):
		return self.question_name 

class Test_case (models.Model):
	#contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	cases = models.CharField(max_length=200)
	def __str__(self):
		return self.cases 
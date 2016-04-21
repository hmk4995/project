from django.db import models


class Question(models.Model):
	question_id= models.IntegerField(default=0)
	question_name = models.CharField(max_length=200, default="", editable=True, unique=True)
	description = models.TextField(max_length=200, default="", editable=True)
	input_format = models.CharField(max_length=200, default="", editable=True)
	output_format = models.CharField(max_length=200, default="", editable=True)
	sample = models.TextField(max_length=200, default="", editable=True)
	score = models.IntegerField(default=0)

	def __str__(self):
		return self.question_name

class Contest(models.Model):
	contest_name = models.CharField(max_length=200, default="", editable=True, unique=True)
	college_name = models.CharField(max_length=200, default="", editable=True, unique=True)
	no_of_candidates = models.IntegerField(default=0)
	no_of_questions = models.IntegerField(default=0)
	time = models.IntegerField(default=0)
	questions = models.CommaSeparatedIntegerField(max_length=200, default=0, editable=True)

	def __str__(self):
		return self.contest_name 


class User(models.Model):
	user_name = models.CharField(max_length=200, default="", editable=True, unique=True)
	password = models.CharField(max_length=200, default="", editable=True)
	admin_privilege = models.CharField(max_length=200, default="", editable=True)
	
	def __str__(self):
		return self.user_name


#class Test_case(models.Model):
#	question = models.ForeignKey(Question, on_delete=models.CASCADE)
#	sl_no = models.IntegerField(default=1, unique=True)
#	inputs = models.CommaSeparatedIntegerField(max_length=200, default="", editable=True)
#	outputs = models.CommaSeparatedIntegerField(max_length=200, default="", editable=True)

#	def __int__(self):
#		return self.sl_no 

class Candidate(models.Model):
	contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
	user_id = models.IntegerField(default=1, unique=True)
	password = models.CharField(max_length=200, default="", editable=True)
	first_name = models.CharField(max_length=200, default="", editable=True)
	last_name = models.CharField(max_length=200, default="", editable=True)

	def __int__(self):
		return self.user_id

class Submission(models.Model):
	candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
	question = models.ForeignKey(Question,default="", on_delete=models.CASCADE)
	language = models.CharField(max_length=200, default="", editable=True)
	time = models.IntegerField(default=0)
	score = models.IntegerField(default=0)

	def __int__(self):
		return self.score


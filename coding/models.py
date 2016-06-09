from django.db import models


class Question(models.Model):
	question_id= models.AutoField(primary_key=True)
	question_name = models.CharField(max_length=200, default="", editable=True, unique=True)
	description = models.TextField(max_length=200, default="", editable=True)
	input_format = models.CharField(max_length=200, default="", editable=True)
	output_format = models.CharField(max_length=200, default="", editable=True)
	sample = models.TextField(max_length=200, default="", editable=True)
	no_of_test_cases = models.IntegerField(default=0)
	score = models.IntegerField(default=0)

	def __str__(self):
		return str(self.question_id)

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

def qstn_test_input_path(self,filename):
	return 'coding/Questions/qstn{0}/inp{1}.txt'.format(self.qno.question_id,self.sl_no)

def qstn_test_output_path(self,filename):
	return 'coding/Questions/qstn{0}/out{1}.txt'.format(self.qno.question_id,self.sl_no)

class Test_case(models.Model):
	qno = models.ForeignKey(Question, on_delete=models.CASCADE)
	sl_no = models.IntegerField(default=1, unique=False)
	inputs = models.FileField(upload_to=qstn_test_input_path,blank=False,null=False)
	outputs = models.FileField(upload_to=qstn_test_output_path,blank=False,null=False)

	def __int__(self):
		return self.sl_no 

class Candidate(models.Model):
	contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
	user_id = models.AutoField(primary_key=True)
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


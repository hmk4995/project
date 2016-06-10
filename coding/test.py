import os
from . import compile as s
from .models import Test_case

def test(path1,name,no):
	path = '/home/Qbuser/Desktop/project/'
	setq =Test_case.objects.filter(qno_id=no)
	cont=Test_case.objects.filter(qno_id=no).count()
	os.chdir(path1)
	cnt=0
	for e in setq:
		compiledResult = s.compil(name,os.path.join(path,e.inputs.name),os.path.join(path,e.outputs.name))
		if (compiledResult =='err'):
			return 'err'
		elif(compiledResult =='Success'):
		   cnt+=1
	return((cnt/cont)*100)

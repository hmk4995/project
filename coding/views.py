from . import test as s
import os
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

#from .models import Document
from .forms import NameForm



def input(request):
	return render(request, 'coding/input.html')



# -*- coding: utf-8 -*-



def upload(request):

	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			cod = form.cleaned_data["code"]
			os.chdir("/home/Qbuser/Desktop/project/coding/contest/nss/nssuser1/ques1/")
			f=open('temp.c','w')
			f.write(cod)
			f.close()
			t=s.test('/home/Qbuser/Desktop/project/coding/contest/nss/nssuser1/ques1/')
			if(t!='err'):
				return HttpResponse(t)
			else:
				f1=open("terr.txt")
				p=f1.read()#.replace('\n', '<br>')
				return HttpResponse("ERRORS\n"+p)
		
		else:
			return HttpResponseRedirect('coding/input.html')

	else:
		#message = 'empty'
		return HttpResponse('/thankyou/')
		
	
	 
	
	  
	
	

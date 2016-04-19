from . import compile as s
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
			f=open('temp.c','w')
			f.write(cod)
			f.close()
			t=s.compile('temp.c','inp.txt','out.txt')
			if(t!='err'):
				return HttpResponse(t)
			else:
				f1=open("terr.txt")
				p=f1.read().replace('\n', '<br>')
				return HttpResponse(p)
		
		else:
			return HttpResponseRedirect('coding/input.html')

	else:
		#message = 'empty'
		return HttpResponse('/thankyou/')
		
	
	 
	
	  
	
	

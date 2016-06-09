from . import test as s
import os
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from coding.models import Question
from .forms import NameForm


def login(request):
    return render_to_response('coding/login')

def list(request):
    info = Question.objects.all()
    detail = {'data':info}
    return render_to_response('coding/list',detail,context_instance=RequestContext(request))

def input(request):
     
            question_info = Question.objects.filter(question_id__exact=request.GET.get('qid'))
            question_detail = {'question_name': question_info}
            return render_to_response('coding/input', question_detail,context_instance=RequestContext(request))

def upload(request):

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            cod = form.cleaned_data["code"]
            idnum = request.POST.get('idno')
            print (idnum)
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
            return HttpResponseRedirect('coding/input')

    else:
        
        return HttpResponse('/thankyou/')
        

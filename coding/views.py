from . import test as s
import os
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from coding.models import Question, Candidate, Contest
from .forms import NameForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse



def login(request):
    return render_to_response('coding/login', context=RequestContext(request))

def list(request):

    if request.method == 'POST':
        uname = request.POST.get('name')
        passwrd = request.POST.get('pword')
        user = authenticate(username = uname, password = passwrd)
        if user is not None:
            if user.is_active:
                if user.is_superuser or user.is_staff:
                    login(request, user)
                    return HttpResponseRedirect(reverse('admin:index'))
        else:
             cand = Candidate.objects.get(user_name__exact=uname)
             if (cand):
                    setw = Contest.objects.get(contest_name__exact=cand.contest)
                    qu = setw.questions.split(',')
                    info = Question.objects.filter(question_id__in=qu)
                    detail = {'data':info}
                    return render_to_response('coding/list',detail,context_instance=RequestContext(request))
             else:
                    return render_to_response('coding/login', context=RequestContext(request))    

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
            lang='c'
            cntst='nss3'
            userid='nssuser1'
            cwd=os.getcwd()
            path='/home/Qbuser/Desktop/project/coding/contest/{0}/{1}/'.format(cntst,userid)
            os.makedirs(path, exist_ok=True)
            os.chdir(path)
            name='temp{0}.{1}'.format(idnum,lang)
            f=open(name,'w')
            f.write(cod)
            f.close()
            os.chdir(cwd)
            t=s.test(path,name,idnum)
            if(t!='err'):
                os.chdir(cwd)
                return HttpResponse(t)
            else:
                f1=open("terr.txt")
                p=f1.read()#.replace('\n', '<br>')
                f1.close()
                os.chdir(cwd)
                return HttpResponse("ERRORS\n"+p)
        
        else:
            return HttpResponseRedirect('coding/input')

    else:
        
        return HttpResponse('/thankyou/')

from . import test as s
import os
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from coding.models import Question, Candidate, Contest
from .forms import NameForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist


def logout_view(request):
    logout(request)
    return redirect('login1')
    
def login1(request):
    return render_to_response('coding/login1', context=RequestContext(request))

def loginauth(request):

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
            try:
                cand = Candidate.objects.get(user_name__exact=uname)
            except ObjectDoesNotExist:
                return redirect('login1')
            return listdis(request,cand)
    else:
        return redirect('login1')

def listdis(request,cand=None):
    if cand is not None:
        setw = Contest.objects.get(contest_name__exact=cand.contest)
    else:
        return redirect('login1')
    qu = setw.questions.split(',')
    info = Question.objects.filter(question_id__in=qu)
    detail = {'data':info}
    return render_to_response('coding/listdis',detail,context_instance=RequestContext(request))
           

def input(request):
    try:
        question_info = Question.objects.filter(question_id__exact=request.GET.get('qid'))
    except ObjectDoesNotExist:
        return redirect('login1')
    question_detail = {'questin_name': question_info}
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
        
        return redirect('login1')

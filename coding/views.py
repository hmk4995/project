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
authfactor=False

def logout_view(request):
    logout(request)
    return redirect('login1')
    
def login1(request):
    return render(request,'coding/login1')

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
                cand = Candidate.objects.get(user_name__exact=uname, password__exact=passwrd)
                print(cand.contest)
            except ObjectDoesNotExist:
                return redirect('login1')
            global authfactor
            authfactor=True
            return redirect('contest',cand.contest,uname)
    else:
        return redirect('login1')

def contest(request,cand=None,uname=None):
    global authfactor
    if(authfactor):
        authfactor=False
        if cand is not None:
            setw = Contest.objects.get(contest_name__exact=cand)
        else:
            return redirect('login1')
        qu = setw.questions.split(',')
        info = Question.objects.filter(question_id__in=qu)
        detail = {'data':info}
        return render(request,'coding/listdis',detail)
    else:
        return redirect('login1')
           

def input(request):
    try:
        question_info = Question.objects.filter(question_id__exact=request.GET.get('qid'))
    except ObjectDoesNotExist:
        return redirect('login1')
    question_detail = {'question_name': question_info}
    return render(request,'coding/input', question_detail)
    

def upload(request):

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            cod = form.cleaned_data["code"]
            idnum = request.POST.get('idno')
            lang = request.POST.get('lan')
            classname = request.POST.get('class')
            request.session['lan'] = lang
            request.session['id'] = idnum
            if(lang=='python'):
                lang = 'py'
            cntst='nss3'
            userid='nssuser1'
            cwd=os.getcwd()
            path='/home/Qbuser/Desktop/project/coding/contest/{0}/{1}/'.format(cntst,userid)
            os.makedirs(path, exist_ok=True)
            os.chdir(path)
            if(lang!='java'):
                name='temp{0}.{1}'.format(idnum,lang)
            else:
                name=classname + '.java'
                print(name)
            f=open(name,'w')
            f.write(cod)
            f.close()
            os.chdir(cwd)
            t=s.test(path, name, idnum, lang, classname)
            if(t!='err'):
                request.session['scr'] = t
                os.chdir(cwd)
                return HttpResponse(t)
            else:
                request.session['scr'] = '0'
                f1=open("terr.txt")
                p=f1.read()#.replace('\n', '<br>')
                f1.close()
                os.chdir(cwd)
                return HttpResponse("ERRORS\n"+p)
        
        else:
            return HttpResponseRedirect('coding/input')

    else:
        
        return redirect('login1')

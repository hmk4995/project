from . import test as s
import os
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from coding.models import Question,Contest
from .forms import NameForm


def login(request):
    return render_to_response('coding/login')

def list(request):
    cntstname='NSS_CONTEST'
    setw = Contest.objects.get(contest_name__exact=cntstname)
    qu = setw.questions.split(',')
    info = Question.objects.filter(question_id__in=qu)
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

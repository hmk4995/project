from . import test as s
import os, shutil
# from coding.templatetags import custom_tags
from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from coding.models import Question, Candidate, Contest, Submission
from .forms import NameForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.contrib import messages
# from django.utils.timezone import utc
# timezone.make_aware(dt_unaware, timezone.get_current_timezone())

 

def logout_view(request):
    logout(request)
    return redirect('login1')
    
def login1(request):
    request.session.set_test_cookie()
    return render(request,'coding/login1')

def loginauth(request):

    if request.method == 'POST':
        # if request.session.test_cookie_worked():
        #     request.session.delete_test_cookie()
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
                    if(cand.finished):
                        messages.error(request, "Your Time is UP!!! {0} has Finished !!".format(cand.contest))
                        return redirect('login1')
                    try:
                        session_name=request.session['namee']
                        session_contest=request.session['contest']
                        print(uname)
                        print(session_name)
                        print(type(uname))
                        print(type(session_name))
                        if session_name!=uname:
                            request.session.flush()
                            print("flush success")
                        else:
                            request.session.set_expiry(cand.remtime)
                            print("redirect success")
                            return redirect('contest',request.session['contest'],request.session['namee'])   
                    except KeyError:
                        print('err')
                    request.session['namee'] = cand.user_name
                    request.session['contest'] = cand.contest
                    if cand.first_name and cand.last_name is not None:
                        request.session.set_expiry(cand.remtime)
                        return redirect('contest',request.session['contest'],request.session['namee'])
                    print(request.session['contest'])
                    print(request.session.keys())
                    print('login')
                    print(request.session.get_expiry_age())
                except ObjectDoesNotExist:
                    messages.error(request, "{0} Does not exist!!!".format(uname))
                    return redirect('login1')
                setw = Contest.objects.get(contest_name__exact=cand.contest)
                if datetime.now(timezone.utc) >= setw.start_date and datetime.now(timezone.utc) <= setw.end_date and request.session.get_expiry_age()!=0:
                    deta = {'dat':setw}
                    return render(request,'coding/details',deta)
                elif datetime.now(timezone.utc) <= setw.start_date:
                    messages.error(request, "{0} has not yet started !!".format(setw.contest_name))
                    return redirect('login1')
                else:
                    messages.error(request, "{0} has Finished !!".format(setw.contest_name))
                    return redirect('login1')

        # else:
        #     messages.error(request, "Please enable cookies and try again.")
        #     return redirect('login1')
    else:
        return redirect('login1')

def contest(request,cand=None,uname=None):
    if cand is not None and uname is not None:
        print(request.session.keys())
        print('contest')
        print(request.session.get_expiry_age())
        try:
            if uname==request.session['namee'] and cand==str(request.session['contest']) and request.session.get_expiry_age()!=0:
                setw = Contest.objects.get(contest_name__exact=cand)
            else:
                messages.error(request, "{0} or {1} Does not Exist !!!".format(cand,uname))
                return redirect('login1')
        except KeyError:
            print("hi again")
            return redirect('login1')
        
        info = setw.questions.all()
        print(info)
        detail = {'data':info, 'cand': request.session['namee']}
        return render(request,'coding/listdis',detail)
    else:
        print("hi")
        return redirect('login1')

def listing(request):
    if request.method == 'POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        print(request.session.keys())
        print('listing')
        print(request.session.get_expiry_age())
        t = Candidate.objects.get(user_name__exact= request.session['namee']) 
        t.first_name = fname
        t.last_name = lname
        t.save()  
        print(fname)
        setw = Contest.objects.get(contest_name__exact=request.session['contest'])
        request.session.set_expiry(t.remtime)
        print (request.session['contest'])
        print(request.session['namee'])
        print(request.session.keys())
        print('listing')
        print(request.session.get_expiry_age())
        return redirect('contest',request.session['contest'],request.session['namee'])        
    # else:
    #     return redirect('login1')
           

def input(request):
    try:
        print(request.session.keys())
        print('input try')
        print(request.session.get_expiry_age())
        question_info = Question.objects.filter(question_id__exact=request.GET.get('qid'))
    except ObjectDoesNotExist:
        return redirect('login1')
    question_detail = {'question_name': question_info, 'cand': request.session['namee']}
    print(request.session.keys())
    print('input')
    print(request.session.get_expiry_age())
    return render(request,'coding/input', question_detail)
    

def upload(request):

    if request.method == 'POST':
        print(request.session.keys())
        print('upload first')
        form = NameForm(request.POST)
        if form.is_valid():
            cod = form.cleaned_data["code"]
            idnum = request.POST.get('idno')
            lang = request.POST.get('lan')
            classname = request.POST.get('class')
            request.session['lan'] = lang
            request.session['id'] = idnum
            print(request.session.keys())
            print('upload second')
            print(request.session.get_expiry_age())
            cntst=str(request.session['contest'])
            userid=request.session['namee']
            cwd=os.getcwd()
            path='/home/Qbuser/Desktop/project/coding/contest/{0}/{1}/'.format(cntst,userid)
            os.makedirs(path, exist_ok=True)
            os.chdir(path)
            if(lang!='java'):
                if(lang=='python'):
                    lang='py'
                name='temp{0}.{1}'.format(idnum,lang)
            else:
                name=classname + '.java'
            f=open(name,'w')
            f.write(cod)
            f.close()
            os.chdir(cwd)
            t=s.test(path, name, idnum, lang, classname)
            if(t=='Program_error'):
                request.session['scr'] = '0'
                f1=open("terr.txt")
                p=f1.read()#.replace('\n', '<br>')
                f1.close()
                os.chdir(cwd)
                return HttpResponse("ERRORS\n"+p)
            elif(t=='compiler_error'):
                request.session['scr'] = '0'
                os.chdir(cwd)
                return HttpResponse(t) 
            elif(t=='Timeout Error'):
                request.session['scr'] = '0'
                os.chdir(cwd)
                return HttpResponse(t)               
            else:
                request.session['scr'] = t
                os.chdir(cwd)
                if(t>0):
                    return HttpResponse("Your program has passed {0}%'' of the testcases".format(t))
                else:
                    return HttpResponse("Your program has failed all of the testcases")

        
        else:
            return HttpResponseRedirect('coding/input')

    else:
        
        return redirect('login1')

def final(request):  
    if request.session.get_expiry_age()>0:
        try:
            score = request.session['scr']
            idnum = request.session['id']
            lang = request.session['lan']
            name = request.session['namee']
        except KeyError:
            print(" final key error")
            return redirect('contest',request.session['contest'],request.session['namee'])  #do something here to prevent simple submit
        del request.session['scr']
        del request.session['id']
        del request.session['lan']
        idno = int(idnum)
        qstnscore=Question.objects.get(question_id__exact=idno)
        scr = int(score*qstnscore.score)/100
        # print(type(scr))
        e = Candidate.objects.get(user_name__exact=name)
        submittime=Contest.objects.get(contest_name__exact=request.session['contest'])
        try:
            submit=Submission.objects.get(candidate__exact=e,question_no__exact=idno)
            if submit.score<scr:
                print("submit score")
                submit.score=scr
                submit.language=lang
                submit.time=submittime.time-timedelta(seconds=request.session.get_expiry_age())
                print(submit.time)
                submit.save()
            else:
                print("submit less error")
                pass
        except ObjectDoesNotExist:
            print("time diff")
            print(submittime.time)
            print(timedelta(request.session.get_expiry_age()))
            print(submittime.time-timedelta(request.session.get_expiry_age()))
            submit=Submission.objects.create(candidate=e,question_no=idno, language=lang, score=scr, time=submittime.time-timedelta(seconds=request.session.get_expiry_age()))
        return redirect('contest',request.session['contest'],request.session['namee'])
    else:
        messages.error(request, "Your Time is UP!!!. {0} has Finished !!".format(request.session['contest']))
        print(request.session['contest'])
        return redirect('contest',request.session['contest'],request.session['namee'])

def ret(request):
    return redirect('contest',request.session['contest'],request.session['namee'])

def logout_candidate(request):
    score=0
    candid=request.GET.get('candid')
    completed=request.GET.get('completed')
    print(completed)
    print('zero')
    # print(completed)
    # request.session.set_expiry(0)
    print(request.session.get_expiry_age())
    print(candid)
    try:
        e = Candidate.objects.get(user_name__exact=candid)
        print(e)
        for i in Submission.objects.filter(candidate__exact=e):
            print(i)
            score+=i.score
        e.scores=score
        e.save()
        print('saved')
    except:
        print("errortry")
    if completed!='complete': 
        e.remtime=timedelta(seconds=request.session.get_expiry_age())
        print('timeout')
    else:
        print("not timeout")
        e.finished=True
        e.remtime=timedelta(seconds=0)
        request.session.flush()
    e.save()
    directory='coding/contest/{0}/{1}/'.format(str(e.contest),e.user_name)
    if os.path.exists(directory):
        shutil.rmtree(directory)
    messages.success(request, "Thank you for taking the test")
    return redirect('login1')

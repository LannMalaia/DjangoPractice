from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from polls.models import LoginTBL
from polls.form.myform import LoginForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            userid = login_form.cleaned_data['userid']
            password = login_form.cleaned_data['password']
            login_result = str()
            try:
                user = LoginTBL.objects.get(user_id=userid)
                if user.password == request.POST['password']:
                    login_result = 'Login Success!!'
                else:
                    login_result = "Password Error!!"
            except LoginTBL.DoesNotExist:
                login_result = 'ID Error!!'
            finally:
                return HttpResponseRedirect(reverse('polls:loginresult', args=(login_result,)))
    else:
        form = LoginForm()
        return render(request, 'polls/index.html', {'form':form})


def logininfo(request):
    login_result = str()
    try:
        user = LoginTBL.objects.get(user_id = request.POST['userid'])
        if user.password == request.POST['password']:
            login_result = 'Login Success!!'
        else:
            login_result = "Password Error!!"
    except LoginTBL.DoesNotExist:
        login_result = 'ID Error!!'
    finally:
        return HttpResponseRedirect(reverse('polls:loginresult', args=(login_result,)))


def result(request, loginresult):
    return render(request, 'polls/result.html', {'loginresult': loginresult})
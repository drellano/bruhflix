from django.shortcuts import render
from forms import LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext


def user_login(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('browse/')
                else:
                    error = "This User has been disabled."
                    return render(request, 'home.html', {'data': data, 'error': error})
            else:
                error = "Incorrect Username or Password"
                return render(request, 'home.html', {'data': data, 'error': error})
        return render(request, 'home.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


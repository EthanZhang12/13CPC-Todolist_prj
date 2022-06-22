# added
from django.utils import timezone
from django.http import HttpResponseRedirect#, HttpResponse, Http404
from django.urls import reverse
from django.views import generic
#from django.template import loader

# modified: shortcuts, get_object_or_404 added
from django.shortcuts import render, get_object_or_404

# added
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
# added
#-
def login1(request):
    # there is a "next" query string in the get request redirected to from a
    # login required view (function), and no "next" in the get request from
    # entering "/accounts/login/" or redirected to from logout; anyway, the
    # login page will be shown
    if request.method == 'GET':
        return render(request, 'login.html', {
            'next': request.GET.get('next', ''),
            'user': request.user, })

    # the post request of submitting the login page, the "next" value is
    # provided by a hidden input element of the form (saved in it by the "next"
    # context object of the login template)
    # user authentication
    user = authenticate(request,
        username=request.POST['username'], password=request.POST['password'])
    # login failed, retry
    if user is None:
        return render(request, 'login.html', {
            'username': request.POST['username'],
            'password': request.POST['password'],
            'next': request.POST['next'],
            'err': True, })

    # let the user login and become the current user (save the user id to the
    # session, which can be get by request.user), and then redirect back to the
    # "next"
    login(request, user)
    if request.POST['next']:
        return HttpResponseRedirect(request.POST['next'])
    return HttpResponseRedirect(reverse('todoList'))

#-
def logout1(request):
    logout(request)
    return HttpResponseRedirect(reverse('todoList'))

#-
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')

    if  User.objects.filter(username=request.POST['username']).count() != 0:
        return render(request, 'signin.html', {
            'username': request.POST['username'],
            'firstname': request.POST['firstname'],
            'lastname': request.POST['lastname'],
            'email': request.POST['email'],
            'password': request.POST['password'],
            'passwdcfm': request.POST['passwdcfm'],
            'err_samename': True, })

    user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
    user.first_name = request.POST['firstname']
    user.last_name = request.POST['lastname']
    user.save()
    login(request, user)
    return HttpResponseRedirect(reverse('todoList'))

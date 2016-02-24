from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

class LoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass

class login_view(TemplateView):
    template_name = 'login.html'
    def post(self, request, *args, **kwargs):
        if self.request.POST:
            if 'submitLogout' in self.request.POST:
                logout(self.request)

            context = self.get_context_data()
            self.template_name = 'login.html'
            uname = request.POST["username"]
            pwd = request.POST["password"]
            
            user = authenticate(username=uname, password=pwd);
            if user is not None:
                if user.is_active:
                    login(self.request, user)
                    context['status'] = 'user is active and now logged in'
                    context['currUser'] = uname
                    return HttpResponseRedirect('/production/cuttingpatterns/retailcuts')
                else:
                    # Return a 'disabled account' error message
                    context['status'] = 'user is not active'
            else:
                # Return an 'invalid login' error message.)
                context['status'] = 'incorrect username or password'

            postData = self.request.POST

        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        if self.request.POST:
            form = LoginForm(self.request.POST)
            if form.is_valid():
                instance = form
        else :
            form = LoginForm()

        uname = 'n/a'
        if self.request.user.is_authenticated():
            uname = self.request.user.get_username()

        return {'form':form, 'status':'', 'currUser': uname}


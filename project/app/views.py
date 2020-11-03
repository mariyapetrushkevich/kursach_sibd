from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from . import forms


# Create your views here.
from django.views.generic import FormView


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = '/app/departments/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect('/app/login/')


class MainView(TemplateView):
    template_name = 'departments.html'

    def get(self, request):
        if request.user.is_authenticated:
            all_departments = Department.objects.all()
            context = {'all_departments': all_departments}
            print(all_departments)

            return render(request, self.template_name, context)
        else:
            return HttpResponseRedirect('/app/login/')


class SpecialitiesView(TemplateView):
    pass


class GroupsView(TemplateView):
    pass


class StudentsView(TemplateView):
    pass


class DisciplinesView(TemplateView):
    pass


class VedomostiView(TemplateView):
    pass


class SpravkiView(TemplateView):
    pass


class AddDepartmentView(TemplateView):
    template_name = 'add_department.html'
    department_form = forms.AddDepartment

    def get(self, request):
        context = {
            'department_form': self.department_form,
        }
        return render(request, self.template_name, context)


def add_department(request):
    form = forms.AddDepartment(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponse("Кафедра добавлена! %s" % request.path)




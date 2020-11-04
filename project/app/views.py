from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
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

            return render(request, self.template_name, context)
        else:
            return HttpResponseRedirect('/app/login/')


class SpecialitiesView(TemplateView):
    template_name = 'specialities.html'
    def get(self, request):
        if request.user.is_authenticated:
            all_specs = Speciality.objects.all()
            context = {'all_specialities': all_specs}

            return render(request, self.template_name, context)


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
            return HttpResponseRedirect('/app/departments/')


def edit_department(request, id):
    try:
        department = Department.objects.get(id=id)

        if request.method == 'POST':
            department.department_name = request.POST.get("department_name")
            department.department_code = request.POST.get("department_code")
            department.save()
            return HttpResponseRedirect('/app/departments/')
        else:
            return render(request, "department_edit.html", {'department': department})
    except Department.DoesNotExist:
        return HttpResponseNotFound("<h2>Такая кафедра не найдена</h2>")


def delete_department(request, id):
    try:
        department = Department.objects.get(id=id)
        department.delete()
        return HttpResponseRedirect("/app/departments")
    except Department.DoesNotExist:
        return HttpResponseNotFound("<h2>Такая кафедра не найдена</h2>")


class AddSpecialityView(TemplateView):
    template_name = 'add_speciality.html'
    form = forms.AddSpeciality

    def get(self, request):
        context = {
            'speciality_form': self.form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = forms.AddSpeciality(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app/specialities')

class EditSpeciality(TemplateView):
    template_name = 'edit_speciality.html'
    form = forms.AddSpeciality

    def get(self, request, id):
        context = {
            'speciality_form': self.form
        }
        return render(request, self.template_name, context)

    def post(self, request, id):
        form = forms.AddSpeciality(request.POST)
        try:
            if form.is_valid():
                speciality = Speciality.objects.get(id=id)
                speciality.speciality_name = form.instance.speciality_name
                speciality.speciality_code = form.instance.speciality_code
                speciality.department = form.instance.department
                speciality.save()
                return HttpResponseRedirect('/app/specialities/')
        except Speciality.DoesNotExist:
            return HttpResponseNotFound("<h2>Такая специальность не найдена</h2>")

def edit_speciality(request, id):
    try:
        speciality = Speciality.objects.get(id=id)

        if request.method == 'POST':
            speciality.speciality_name = request.POST.get("speciality_name")
            speciality.speciality_code = request.POST.get("speciality_code")
            speciality.department = request.POST.get("department")
            speciality.save()
            return HttpResponseRedirect('/app/specialities/')
        else:
            return render(request, "speciality_edit.html", {'speciality': speciality})
    except Speciality.DoesNotExist:
        return HttpResponseNotFound("<h2>Такая специальность не найдена</h2>")


def delete_speciality(request, id):
    try:
        speciality = Speciality.objects.get(id=id)
        speciality.delete()
        return HttpResponseRedirect("/app/specialities")
    except Department.DoesNotExist:
        return HttpResponseNotFound("<h2>Такая Специальность не найдена</h2>")

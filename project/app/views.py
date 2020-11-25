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
    template_name = 'groups.html'
    def get(self, request):
        if request.user.is_authenticated:
            all_groups = Group.objects.all()
            context = {'all_groups': all_groups}

            return render(request, self.template_name, context)


class StudentsView(TemplateView):
    template_name = 'students.html'
    def get(self, request):
        if request.user.is_authenticated:
            all_students = Student.objects.all()
            context = {'all_students': all_students}

            return render(request, self.template_name, context)


class DisciplinesView(TemplateView):
    template_name = 'disciplines.html'
    def get(self, request):
        if request.user.is_authenticated:
            all_disciplines = Discipline.objects.all()
            context = {'all_disciplines': all_disciplines}

            return render(request, self.template_name, context)


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

    def post(self, request):
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

class EditSpecialityView(TemplateView):
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


def delete_speciality(request, id):
    try:
        speciality = Speciality.objects.get(id=id)
        speciality.delete()
        return HttpResponseRedirect("/app/specialities")
    except Department.DoesNotExist:
        return HttpResponseNotFound("<h2>Такая Специальность не найдена</h2>")


class AddGroupView(TemplateView):
    template_name = 'add_group.html'
    form = forms.AddGroup

    def get(self, request):
        context = {
            'group_form': self.form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = forms.AddGroup(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app/groups')


class EditGroupView(TemplateView):
    template_name = 'edit_group.html'
    form = forms.AddGroup

    def get(self, request, id):
        context = {
            'group_form': self.form
        }
        return render(request, self.template_name, context)

    def post(self, request, id):
        form = forms.AddGroup(request.POST)
        try:
            if form.is_valid():
                group = Group.objects.get(id=id)
                group.group_number = form.instance.group_number
                group.speciality = form.instance.speciality
                group.form_year = form.instance.form_year
                group.course = form.instance.course
                group.form_of_learning = form.instance.form_of_learning
                group.save()
                return HttpResponseRedirect('/app/specialities/')
        except Speciality.DoesNotExist:
            return HttpResponseNotFound("<h2>Такая группа не найдена</h2>")


def delete_group(request, id):
    try:
        group = Group.objects.get(id=id)
        group.delete()
        return HttpResponseRedirect("/app/groups")
    except Department.DoesNotExist:
        return HttpResponseNotFound("<h2>Такая группа не найдена</h2>")


class AddStudentView(TemplateView):
    template_name = 'add_student.html'
    form = forms.AddStudent

    def get(self, request):
        context = {
            'student_form': self.form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = forms.AddStudent(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app/students')


class EditStudentView(TemplateView):
    template_name = 'edit_student.html'
    form = forms.AddStudent

    def get(self, request, id):
        context = {
            'student_form': self.form
        }
        return render(request, self.template_name, context)

    def post(self, request, id):
        form = forms.AddStudent(request.POST)
        try:
            if form.is_valid():
                student = Student.objects.get(id=id)
                student.surname = form.instance.surname
                student.first_name = form.instance.first_name
                student.patronymic = form.instance.patronymic
                student.group = form.instance.group
                student.stud_number = form.instance.stud_number
                student.address = form.instance.address
                student.avg_score = form.instance.avg_score
                student.save()
                return HttpResponseRedirect('/app/students/')
        except Student.DoesNotExist:
            return HttpResponseNotFound("<h2>Такой студент не найдена</h2>")


def delete_student(request, id):
    try:
        student = Student.objects.get(id=id)
        student.delete()
        return HttpResponseRedirect("/app/students")
    except Student.DoesNotExist:
        return HttpResponseNotFound("<h2>Такой студент не найден</h2>")


class AddDisciplineView(TemplateView):
    template_name = 'add_discipline.html'
    form = forms.AddDiscipline

    def get(self, request):
        context = {
            'discipline_form': self.form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = forms.AddDiscipline(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app/disciplines')


class EditDisciplineView(TemplateView):
    template_name = 'edit_discipline.html'
    form = forms.AddDiscipline

    def get(self, request, id):
        context = {
            'discipline_form': self.form
        }
        return render(request, self.template_name, context)

    def post(self, request, id):
        form = forms.AddDiscipline(request.POST)
        try:
            if form.is_valid():
                discipline = Discipline.objects.get(id=id)
                discipline.discipline_name = form.instance.discipline_name
                discipline.teachers = form.instance.teachers
                discipline.form_of_attestation = form.instance.form_of_attestation
                discipline.save()
                return HttpResponseRedirect('/app/disciplines/')
        except Student.DoesNotExist:
            return HttpResponseNotFound("<h2>Такая дисциплина не найдена</h2>")


def delete_discipline(request, id):
    try:
        discipline = Discipline.objects.get(id=id)
        discipline.delete()
        return HttpResponseRedirect("/app/disciplines")

    except Discipline.DoesNotExist:
        return HttpResponseNotFound("<h2>Такая дисциплина не найдена</h2>")

from django.forms import ModelForm, Form
from django import forms
from .models import *


class AddDepartment(ModelForm):
    class Meta:
        model = Department
        fields = ['department_name', 'department_code']


class AddSpeciality(ModelForm):
    class Meta:
        model = Speciality
        fields = ['speciality_name', 'speciality_code', 'department']


class AddGroup(ModelForm):
    class Meta:
        model = Group
        fields = ['group_number', 'speciality', 'form_year', 'course', 'form_of_learning']
        
        
class AddStudent(ModelForm):
    class Meta:
        model = Student
        fields = ['surname', 'first_name', 'patronymic', 'group', 'stud_number', 'address', 'avg_score']


class AddDiscipline(ModelForm):
    class Meta:
        model = Discipline
        fields = ['discipline_name', 'teachers', 'form_of_attestation']


class AddVedomost(ModelForm):
    class Meta:
        model = Vedomost
        fields = ['discipline', 'student_keeper', 'vedomost_name']
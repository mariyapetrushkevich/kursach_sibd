from django.forms import ModelForm, Form
from django import forms
from .models import *


class AddDepartment(ModelForm):
    class Meta:
        model = Department
        fields = ['department_name', 'department_code']
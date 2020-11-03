"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginFormView.as_view()),
    path('departments/', views.MainView.as_view()),
    path('logout/', views.LogoutView.as_view),
    path('specialities/', views.SpecialitiesView.as_view()),
    path('groups/', views.GroupsView.as_view()),
    path('students/', views.StudentsView.as_view()),
    path('disciplines/', views.DisciplinesView.as_view()),
    path('vedomosti/', views.VedomostiView.as_view()),
    path('spravki/', views.SpravkiView.as_view()),
    path('add-department-form/', views.AddDepartmentView.as_view()),
    path('add-department/', views.add_department),
    path('department_edit/<int:id>/', views.edit_department),
    path('department_delete/<int:id>/', views.delete_department),
    path('add-speciality-form/', views.AddSpecialityView.as_view()),
    # path('speciality_edit/<int:id>/', views.edit_speciality),
    # path('speciality_delete/<int:id>/', views.delete_speciality),
]

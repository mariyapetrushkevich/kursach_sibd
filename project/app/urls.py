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
    path('', views.LoginFormView.as_view()),
    path('departments/', views.MainView.as_view()),
    path('logout/', views.LogoutView.as_view),
    path('specialities/', views.SpecialitiesView.as_view()),
    path('groups/', views.GroupsView.as_view()),
    path('students/', views.StudentsView.as_view()),
    path('disciplines/', views.DisciplinesView.as_view()),
    path('vedomosti/', views.VedomostiView.as_view()),
    path('spravki/', views.SpravkiView.as_view()),
    path('add-department-form/', views.AddDepartmentView.as_view()),
    path('department_edit/<int:id>/', views.edit_department),
    path('department_delete/<int:id>/', views.delete_department),
    path('add-speciality-form/', views.AddSpecialityView.as_view()),
    path('speciality_edit/<int:id>/', views.EditSpecialityView.as_view()),
    path('speciality_delete/<int:id>/', views.delete_speciality),
    path('add_group', views.AddGroupView.as_view()),
    path('group_edit/<int:id>/', views.EditGroupView.as_view()),
    path('group_delete/<int:id>/', views.delete_group),
    path('add_student', views.AddStudentView.as_view()),
    path('student_edit/<int:id>/', views.EditStudentView.as_view()),
    path('student_delete/<int:id>/', views.delete_student),
    path('add_discipline/', views.AddDisciplineView.as_view()),
    path('edit_discipline/<int:id>/', views.EditDisciplineView.as_view()),
    path('delete_discipline/<int:id>/', views.delete_discipline),
    path('add_vedomost/', views.AddVedomostView.as_view()),
    path('delete_vedomost/<int:id>/', views.delete_vedomost),
    path('add_spravka/', views.AddSpravkaView.as_view()),
    path('delete_spravka/<int:id>/', views.delete_spravka),
    path('student_search_result', views.StudentSearchResultView.as_view()),
    path('student_stud_filter', views.FilteredStudentView.as_view()),
    path('student_sorted_asc', views.StudentSortedAsc.as_view()),
    path('student_sorted_desc', views.StudentSortedDesc.as_view()),
    path('filter_group', views.FilterGroup.as_view())
]

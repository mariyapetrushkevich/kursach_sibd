from django.db import models

# Create your models here.


class Department(models.Model):
    department_name = models.CharField(max_length=70, null=True, verbose_name='Название')
    department_code = models.CharField(max_length=10, null=True, verbose_name='Код кафедры')

    def __str__(self):
        return self.department_name


class Speciality(models.Model):
    department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Кафедра')
    speciality_name = models.CharField(max_length=100, null=True, verbose_name='Специальность')
    speciality_code = models.CharField(max_length=20, null=True, verbose_name='Код специальности')

    def __str__(self):
        return self.speciality_name


class Group(models.Model):
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, verbose_name='Специальность')
    group_number = models.IntegerField(verbose_name='Номер группы')
    form_year = models.IntegerField(verbose_name='Год формирования')
    course = models.SmallIntegerField(verbose_name='Курс')
    form_of_learning = models.CharField(max_length=10)

    def __str__(self):
        return self.group_number


class Student(models.Model):
    group = models.ForeignKey(Speciality, on_delete=models.CASCADE, verbose_name='Группа')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    patronymic = models.CharField(max_length=20, verbose_name='Отчество')
    stud_number = models.CharField(max_length=15, verbose_name='Номер студенческого билета')
    address = models.CharField(max_length=50, verbose_name='Адрес')
    avg_score = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='Средний балл')

    def __str__(self):
        return self.first_name + self.surname


class Discipline(models.Model):
    discipline_name = models.CharField(max_length=50, verbose_name='Название дисциплины')
    teachers = models.CharField(max_length=60, verbose_name='Преподаватели')
    form_of_attestation = models.CharField(max_length=10, verbose_name='Форма аттестации')

    def __str__(self):
        return self.discipline_name


class Vedomost(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name='Дисциплина')
    student_keeper = models.ManyToManyField(Student, verbose_name='Студент-заказчик')
    vedomost_name = models.CharField(max_length=50, default='Зачётная', verbose_name='Назначение ведомости')

    def __str__(self):
        return self.vedomost_name

class Spravki(models.Model):
    student_keeper = models.ManyToManyField(Student, verbose_name='Студент-заказчик')
    spravka_name = models.CharField(max_length=20, verbose_name='Назначение справки')

    def __str__(self):
        return self.spravka_name


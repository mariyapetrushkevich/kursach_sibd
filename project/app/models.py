from django.db import models

# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=50, )
    department_code = models.IntegerField()

    def __str__(self):
        return self.department_name


class Speciality(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    speciality_name = models.CharField(max_length=50)
    speciality_code = models.IntegerField()

    def __str__(self):
        return self.speciality_name


class Group(models.Model):
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    group_number = models.IntegerField()
    form_year = models.IntegerField()
    course = models.SmallIntegerField()
    form_of_learning = models.CharField(max_length=10)

    def __str__(self):
        return self.group_number


class Student(models.Model):
    group = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    surname = models.CharField(max_length=30)
    first_name = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    stud_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    avg_score = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.first_name + self.surname


class Discipline(models.Model):
    discipline_name = models.CharField(max_length=50)
    teachers = models.CharField(max_length=60)
    form_of_attestation = models.CharField(max_length=10)

    def __str__(self):
        return self.discipline_name


class Vedomost(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    student_keeper = models.ManyToManyField(Student)
    vedomost_name = models.CharField(max_length=50)

    def __str__(self):
        return self.vedomost_name

class Spravki(models.Model):
    student_keeper = models.ManyToManyField(Student)
    spravka_name = models.CharField(max_length=20)

    def __str__(self):
        return self.spravka_name


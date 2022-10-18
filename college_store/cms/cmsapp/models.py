from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


FRUIT_CHOICES = [
    ('Enquiry', 'Enquiry'),
    ('Place order', 'Place order'),
    ('Return', 'Return'),

]
GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),

]


class Person(models.Model):
    name = models.CharField(max_length=124)
    date_of_birth = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    phone = models.IntegerField()
    mail_id = models.EmailField(max_length=200)
    address = models.TextField()
    purpose = models.CharField(choices=FRUIT_CHOICES, max_length=200)
    materials = models.CharField(max_length=250)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course,  on_delete=models.CASCADE, blank=True, null=True, default=None)

    def __str__(self):
        return self.name

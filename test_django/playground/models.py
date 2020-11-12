from django.db import models
from django.db.models.signals import post_save


UNIVERSITY_DOMAIN = 'ourdomain.edu'

# Create your models here.

class StudentInformation(models.Model):
    class Meta:
        verbose_name = "StudentInformation"
        verbose_name_plural = "StudentInformations"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pass_id = models.CharField(max_length=10, unique=True)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class StudentInfo(models.Model):
    class Meta:
        verbose_name = "StudentInfo"
        verbose_name_plural = "StudentInfos"

    pass_id = models.CharField(unique=True, null=True, max_length=50)
    email = models.EmailField(unique=True)
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='info'
    )

    def __str__(self):
        return f'{self.pass_id}'


def create_student_info(instance, created, **kwargs):
    if not created:
        return
    count = Student.objects.filter(first_name=instance.first_name).count()
    new_email = f'{instance.first_name.lower()}{count}@{UNIVERSITY_DOMAIN}'
    StudentInfo.objects.create(student=instance, email=new_email)


post_save.connect(create_student_info, sender=Student)

#

class Publisher(models.Model):
    class Meta:
        verbose_name = "Publisher"
        verbose_name_plural = "Publishers"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Article(models.Model):
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    title = models.CharField(max_length=250)
    # body = models.TextField()
    pub_date = models.DateField()
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.title} on {self.pub_date}'

#


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title


class Shop(models.Model):
    class Meta:
        verbose_name = "Shop"
        verbose_name_plural = "Shops"

    title = models.CharField(max_length=50)
    # address
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

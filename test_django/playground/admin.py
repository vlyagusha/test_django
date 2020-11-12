from django.contrib import admin

# Register your models here.
from .models import Student, StudentInfo, Publisher, Article

admin.site.register(Student)
admin.site.register(Publisher)
admin.site.register(Article)


@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ('pass_id', 'email', 'student')

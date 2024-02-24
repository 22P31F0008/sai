from django.contrib import admin
from .models import course
from .models import student_details
# Register your models here.

admin.site.register(course)
admin.site.register(student_details)
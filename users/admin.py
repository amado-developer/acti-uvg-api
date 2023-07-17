from django.contrib import admin

from django.contrib import admin
from .models import User, Student, Director, Organization

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Director)
admin.site.register(Organization)

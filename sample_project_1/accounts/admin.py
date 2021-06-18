from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Student)
admin.site.register(Post)
admin.site.register(Student_post)
admin.site.register(Comment)
from django.contrib import admin
from students.models import Student, Activitylist ,Teacher

admin.site.register(Student),
admin.site.register(Teacher),
admin.site.register(Activitylist)

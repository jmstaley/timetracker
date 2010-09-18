from django.contrib import admin
from models import Task, Work

class TaskAdmin(admin.ModelAdmin):
    pass

admin.site.register(Task, TaskAdmin)

class WorkAdmin(admin.ModelAdmin):
    pass

admin.site.register(Work, WorkAdmin)


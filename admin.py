from django.contrib import admin
from models import Task, Work

class TaskAdmin(admin.ModelAdmin):
    fieldsets = ( (None, {'fields': ('title', 'description', 'author')}),
                  ('Extra info', {'classes': ('collapse',),
                                  'fields': ('due_date',)}) )

admin.site.register(Task, TaskAdmin)

class WorkAdmin(admin.ModelAdmin):
    pass

admin.site.register(Work, WorkAdmin)


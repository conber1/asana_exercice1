from django.contrib import admin
from .models import *


class ProjectAdmin(admin.ModelAdmin):
    list_display, fields = ('project_name',), ('project_name',)

class UserAdmin(admin.ModelAdmin):
    list_display, fields = ('user_name', 'user_email'), ('user_name', 'user_email') #List of fields which are displaying in django admin

class TaskAdmin(admin.ModelAdmin):
    list_display, exclude = ('task_name', 'project_link', 'executor_link'), ('task_id',) #The same, the exclude tuple removing the field from django admin

admin.site.register(Project, ProjectAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Task, TaskAdmin)

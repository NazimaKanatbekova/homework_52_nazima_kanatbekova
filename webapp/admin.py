from django.contrib import admin

from webapp.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'status', 'date')
    list_filter = ('date', 'status')

admin.site.register(Task, TaskAdmin)


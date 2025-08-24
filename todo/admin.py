from django.contrib import admin
from . models import Todo
from django.contrib import admin
from .models import Student

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'index', 'due_date', 'created_at', 'completed')
    search_fields = ('title', 'description')
    list_filter = ('completed', 'due_date')
admin.site.register(Todo, TodoAdmin)
admin.site.register(Student)
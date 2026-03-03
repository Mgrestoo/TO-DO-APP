from django.contrib import admin
from .models import Task, Category, TaskCategory, UserProfile
from tasks import models

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__username',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    
class TaskCategoryInline(admin.TabularInline):
    model = TaskCategory
    extra = 1
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_completed', 'created_at')
    list_filter = ('is_completed', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at',)
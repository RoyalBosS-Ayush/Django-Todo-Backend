from django.contrib import admin
from .models import TodoItem, Tag


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ("title", "timestamp", "status")
    list_filter = ("status",)
    search_fields = ("title", "description")
    readonly_fields = ("timestamp",)
    fieldsets = (
        (
            "Task Information",
            {"fields": ("title", "description", "due_date", "tags", "status")},
        ),
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)

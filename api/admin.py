from django.contrib import admin

# Register your models here.
from .models import *
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','status')
    list_filter = ("title",)
    prepopulated_fields={'slug': ('title',)}
    search_fields = ['title',]

admin.site.register(Project)
admin.site.register(Client)
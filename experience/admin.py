from django.contrib import admin
from .models import Experience

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'exp_type', 'start_date', 'end_date', 'order')
    list_filter  = ('exp_type',)

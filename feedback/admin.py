from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'created_at')
    search_fields = ('user_name', 'email')

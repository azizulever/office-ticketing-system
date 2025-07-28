from django.contrib import admin
from .models import Ticket, TicketFeedback


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'employee', 'priority', 'status', 'created_at']
    list_filter = ['status', 'priority', 'created_at']
    search_fields = ['title', 'employee__username']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(TicketFeedback)
class TicketFeedbackAdmin(admin.ModelAdmin):
    list_display = ['ticket', 'admin_user', 'created_at']
    list_filter = ['created_at']
    search_fields = ['ticket__title', 'admin_user__username']

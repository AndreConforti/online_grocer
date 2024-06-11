from django.contrib import admin
from .models import ReceivedMessages


@admin.register(ReceivedMessages)
class ListReceivedMessages(admin.ModelAdmin):
    readonly_fields=('name', 'email', 'message', 'date')
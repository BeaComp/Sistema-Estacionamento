from customer.models import Customer
from django.contrib import admin


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'cpf', 'phone', 'created_at']
    search_fields = ['name', 'cpf', 'phone']

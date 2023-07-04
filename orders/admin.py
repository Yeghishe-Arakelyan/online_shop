from django.contrib import admin
from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'status', 'get_total_price')
    list_filter = ('status',)
    search_fields = ('user__username', 'user__email', 'user__full_name')
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)

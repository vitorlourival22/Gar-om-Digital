from django.contrib import admin
from .models import Table, Order, OrderItem

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'status')
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'status', 'mesaId')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('orderId', 'itemId', 'quantity', 'unitPrice')


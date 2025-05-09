from django.db import models
from menu.models import Item

class Table(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'tables'

    def __str__(self):
        return f'Table {self.number}'

class Order(models.Model):
    STATUS_CHOICES = [
        ('P', 'Preparing'),
        ('S', 'Served'),
        ('C', 'Cancelled'),
    ]

    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    mesaId = models.ForeignKey(Table, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'orders'

class OrderItem(models.Model):
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True)
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True)
    quantity = models.IntegerField()
    unitPrice = models.FloatField()

    class Meta:
        db_table = 'order_items'

from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def add_stock(self, quantity):
        self.stock += quantity
        self.save()

    def remove_stock(self, quantity):
        if quantity > self.stock:
            raise ValueError("Not enough stock!")
        self.stock -= quantity
        self.save()

class StockMovement(models.Model):
    MOVEMENT_TYPES = [
        ('in', 'Stock In'),
        ('out', 'Stock Out'),
    ]

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_TYPES)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        #Atualiza o estoque ao registrar um movimento
        if self.movement_type == 'in':
            self.item.add_stock(self.quantity)
        elif self.movement_type == 'out':
            self.item.remove_stock(self.quantity)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_movement_type_display()} - {self.item.name} ({self.quantity})"
    
    class Cart(models.Model):
        product = models.ForeignKey(Item,on_delete=models.CASCADE)

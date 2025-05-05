from django import forms
from .models import StockMovement, Item, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name',]
        
class StockMovementForm(forms.ModelForm):
    class Meta:
        model = StockMovement
        fields = ['item', 'quantity', 'movement_type']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'category']  # Added category field

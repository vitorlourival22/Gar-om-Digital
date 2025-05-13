"""URL configuration for config project."""

from django.contrib import admin
from django.urls import path

from menu.views import item_list, stock_movement, add_item, home, menu, item_menu, add_category,Add_cart,view_cart,remove_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('item_list/', item_list, name='item_list'),
    path('stock-movement/', stock_movement, name='stock_movement'),
    path('add_item/', add_item, name='add_item'),
    path('item_menu/', item_menu, name='item_menu'),
    path('add_category/', add_category, name='add_category'),  # Corrected to use a string for the name
    path('cart/',view_cart, name='view_cart'),
    path('cart/add/<int:item_id>/',Add_cart, name='add_cart'),
    path('cart/remove/<int:item_id>/',remove_cart, name='remove_cart'),
]
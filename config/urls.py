"""URL configuration for config project."""

from django.contrib import admin
from django.urls import path
from menu.views import item_list, stock_movement, add_item, home, menu, item_menu, add_category,Add_cart,view_cart,remove_cart,cardapio_gestor
from orders.views import create_qr_code, show_table,add_table,list_tables,delete_table,garcom,status

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('item_list/', item_list, name='item_list'),
    path('stock-movement/', stock_movement, name='stock_movement'),
    path('add_item/', add_item, name='add_item'),
    path('item_menu/', item_menu, name='item_menu'),
    path('add_category/', add_category, name='add_category'),  
    path('cart/',view_cart, name='view_cart'),
    path('cart/add/<int:item_id>/', Add_cart, name='add_cart'),
    path('cart/remove/<int:item_id>/',remove_cart, name='remove_cart'),
    path('create_qr_code/<int:table_id>/', create_qr_code, name='create_qr_code'),
    path('show_table/<int:table_id>/', show_table, name='show_tables'),
    path('add_table/', add_table, name='add_table'),
    path('list-tables/', list_tables, name='list_tables'),
    path('delete-table/<int:table_id>/', delete_table, name='delete_table'),
    path('garcom/', garcom, name='garcom'),
    path('cardapio_gestor/', cardapio_gestor, name='cardapio_gestor'),
    path('status/', status, name='status'),
]
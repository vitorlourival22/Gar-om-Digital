from django.shortcuts import render, redirect,get_object_or_404
from .models import Item, StockMovement
from .forms import StockMovementForm,ItemForm,CategoryForm

def home(request):
    return render(request, 'home.html')

def menu(request):
    items = Item.objects.all()
    return render(request, 'menu.html', {'items': items})
def item_menu(request):
    items = Item.objects.all()
    return render(request, 'item_menu.html', {'items': items})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'inventory/item_list.html', {'items': items})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'add_category.html', {'form': form})
    else:
        form = CategoryForm()  # Create a new form instance for GET requests
        return render(request, 'add_category.html', {'form': form})  # Pass the empty form to the template


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_menu')
        else:
            return render(request, 'add_item.html', {'form': form})
    else:
        form = ItemForm()  # Create a new form instance for GET requests
        return render(request, 'add_item.html', {'form': form})  # Pass categories to the template




def stock_movement(request):
    if request.method == 'POST':
            form.save()
            return redirect('item_list')
    else:
        form = StockMovementForm()
    return render(request, 'inventory/stock_movement.html', {'form': form})

def Add_cart(request,item_id):
    item = get_object_or_404(Item,id=item_id)
    cart = request.session.get('cart',{})

    item_id_str = str(item.id)
    if item_id_str not in cart:
        cart[item_id_str] = {'nome': item.name, 'quantity': 1,'price': str(item.price)}
    else:
        cart[item_id_str]['quantity'] += 1

        request.session["cart"] = cart
        request.session.modified = True
        return redirect('View_cart')
    
def remove_cart(request, item_id):
    cart = request.session.get('cart', {})
    item_id_str = str(item_id)

    if item_id_str in cart:
        del cart[item_id_str]
        request.session['cart'] = cart
        request.session.modified = True

    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    total = sum(float(item['price']) * item['quantity'] for item in cart.values())
    return render(request, 'cart.html', {'cart': cart, 'total': total})

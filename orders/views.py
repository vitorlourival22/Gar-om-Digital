import qrcode
from django.shortcuts import render, redirect
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404, redirect
from .models import Table
from .forms import TableForm

def create_qr_code(request, table_id):
    table = Table.objects.get(id=table_id)
    url = f'http://127.0.0.1:8000/table/{table.id}'

    qr = qrcode.make(url)
    img_io = BytesIO()
    qr.save(img_io, 'PNG')
    img_io.seek(0)
    
    return HttpResponse(img_io, content_type='image/png')


def show_table(request, table_id):
    table = Table.objects.get(id=table_id)
    qr_code_url = f'/create_qr_code/{table.id}/'
    
    return render(request, 'table/detalhes.html', {'mesa': table, 'qr_code_url': qr_code_url})

def add_table(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tables')  # Ou para a página que desejar
        else:
            return render(request, 'add_table.html', {'form': form})
    else:
        form = TableForm()
        return render(request, 'add_table.html', {'form': form})
from .models import Table  # Importe o modelo se ainda não fez

def list_tables(request):
    tables = Table.objects.all().order_by('number')  # Você pode ordenar como quiser
    return render(request, 'list_tables.html', {'tables': tables})

def delete_table(request, table_id):
    table = get_object_or_404(Table, id=table_id)
    if request.method == 'POST':
        table.delete()
        return redirect('list_tables')  # Redireciona para a lista após excluir
    return render(request, 'confirm_delete.html', {'table': table})

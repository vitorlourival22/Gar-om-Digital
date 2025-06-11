import qrcode
from django.shortcuts import render, redirect
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404, redirect
from .models import Table
from .forms import TableForm
from django.core.files import File

def garcom(request):
    return render(request, 'garcom.html')

def status(request):
    return render(request, 'Preparo.html')

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
    
    return render(request, 'detalhes.html', {'mesa': table, 'qr_code_url': qr_code_url})

def add_table(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            table = form.save(commit=False)
            table.save()  # Salva a mesa para ter um ID

            # Gera o QR code com a URL da mesa
            url = f'http://127.0.0.1:8000/table/{table.id}'
            qr = qrcode.make(url)
            
            img_io = BytesIO()
            qr.save(img_io, 'PNG')
            img_io.seek(0)
            
            # Salva o arquivo de imagem no campo qr_code_image
            filename = f'table_{table.id}_qr.png'
            table.qr_code_image.save(filename, File(img_io), save=True)
            
            return redirect('list_tables')  # Ou para a página que desejar
        else:
            return render(request, 'add_table.html', {'form': form})
    else:
        form = TableForm()
        return render(request, 'add_table.html', {'form': form})

def list_tables(request):
    tables = Table.objects.all().order_by('number')  # Você pode ordenar como quiser
    
    return render(request, 'list_tables.html', {'tables': tables})

def delete_table(request, table_id):
    table = get_object_or_404(Table, id=table_id)
    if request.method == 'POST':
        table.delete()
        return redirect('list_tables')  # Redireciona para a lista após excluir
    return render(request, 'confirm_delete.html', {'table': table})

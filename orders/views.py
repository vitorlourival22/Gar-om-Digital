import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render
from .models import Table

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
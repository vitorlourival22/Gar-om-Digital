from django import forms
from .models import Table
class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['number', 'status']

    def clean_number(self):
        number = self.cleaned_data['number']
        if Table.objects.filter(number=number).exists():
            raise forms.ValidationError("Já existe uma mesa com esse número.")
        return number
# user/forms.py
from django import forms

class CadastroForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    whatsapp = forms.CharField(label='WhatsApp', max_length=15)

class ServicosForm(forms.Form):
    SERVICOS_CHOICES = [
        ('cafe_manha', 'Café da Manhã'),
        ('almoco', 'Almoço'),
        ('jantar', 'Jantar'),
        ('sobremesas', 'Sobremesas'),
        ('comida_internacional', 'Comida Internacional')
    ]
    servicos = forms.MultipleChoiceField(
        choices=SERVICOS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Serviços Disponíveis"
    )
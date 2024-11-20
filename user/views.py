from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CadastroForm, ServicosForm  # Importa o formulário que iremos criar
from django.urls import reverse

# Create your views here.

def login_view(request):
    return render(request, 'registration/login.html')

def calendario(request):
    
    return render(request, 'calendario.html')


def cadastro(request):
    # Captura a data selecionada enviada pelo calendário
    data_selecionada = request.GET.get('data', 'Não informada')

    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            # Lógica de salvar ou redirecionar
            return redirect('contratar_servicos')
    else:
        form = CadastroForm()

    return render(request, 'cadastro.html', {'form': form, 'data_selecionada': data_selecionada})


def contratar_servicos(request):
    if request.method == 'POST':
        # Captura os dados enviados via POST
        data_selecionada = request.POST.get('data_selecionada', 'Não informada')
        nome = request.POST.get('nome', 'Nome não informado')
        email = request.POST.get('email', 'Email não informado')
        whatsapp = request.POST.get('whatsapp', 'WhatsApp não informado')
        servicos = request.POST.getlist('servicos')  # Captura a lista de serviços selecionados

        # Redireciona para a página de confirmação passando os dados via query string
        url = f"{reverse('confirmacao')}?data_selecionada={data_selecionada}&nome={nome}&email={email}&whatsapp={whatsapp}"
        for servico in servicos:
            url += f"&servicos={servico}"
        return HttpResponseRedirect(url)
    
    # Se não for POST, renderiza a página de contratação novamente
    servicos = ["Cozinha Internacional", "Comida Vegana", "Sobremesas", "Serviço de Limpeza", "Serviço de Bebidas"]
    return render(request, 'contratar_servicos.html', {'servicos': servicos})

def confirmacao(request):
    # Obtém os dados passados pela query string
    data_selecionada = request.GET.get('data_selecionada', 'Não informada')
    nome = request.GET.get('nome', 'Nome não informado')
    email = request.GET.get('email', 'Email não informado')
    whatsapp = request.GET.get('whatsapp', 'WhatsApp não informado')
    servicos = request.GET.getlist('servicos')  # Lista de serviços selecionados

    return render(request, 'confirmacao.html', {
        'data_selecionada': data_selecionada,
        'nome': nome,
        'email': email,
        'whatsapp': whatsapp,
        'servicos': servicos
    })

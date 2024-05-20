from django.shortcuts import render
from postgresql import models
import requests

# Create your views here.

def index(request):
    return render(request, 'postgresql/index.html')

def comparativo(request):
    planos = models.Planos.objects.all()
    return render(request, 'postgresql/comparativo.html', {'planos': planos},)

def sobre(request):
    return render(request, 'postgresql/sobre.html')

def contato(request):
    return render(request, 'postgresql/contato.html')

def filtros(request):
    f_operadora = request.GET.get('operadoras', '')
    f_plano = request.GET.get('planos', '')
    f_ordem = request.GET.get('filtro', '')
    f_cep = str(request.GET.get('cep', ''))

    planos = models.Planos.objects.filter(apelido__icontains=f_operadora)

    if f_plano == 'satelite':
        planos = planos.filter(satelite=True)
    elif f_plano == 'fibra':
        planos = planos.filter(fibra=True)

    if f_ordem == 'menor-preco':
        planos = planos.order_by('preco')
    elif f_ordem == 'maior-velocidade':
        planos = planos.order_by('-velocidade')
    else:
        planos = planos.order_by('apelido')

    if f_cep:
        f_cep = f_cep.replace('-', '').replace('.', '').replace('', '')
        if len(f_cep) == 8:
            url = f'https://viacep.com.br/ws/{f_cep}/json/'
            response = requests.get(url)
            if response.status_code == 200:
                dic_endereco = response.json()
                if len(dic_endereco) == 1:
                    cep_nao_encontrado = 'Cep não encontrado'
                    return render(request, 'postgresql/filtros.html', {'planos': planos, 'cep_nao_encontrado': cep_nao_encontrado})
                else:
                    informacoes_endereco = f"{dic_endereco['logradouro']}, {dic_endereco['bairro']} | {dic_endereco['localidade']} - {dic_endereco['uf']} - CEP: {dic_endereco['cep']}"
                    if dic_endereco['localidade'] == 'Guarujá':
                        return render(request, 'postgresql/filtros.html', {'planos': planos, 'informacoes_endereco': informacoes_endereco})
                    else:
                        planos = []
                        fora_de_alcance = 'Endereço fora da área de cobertura da plataforma.'
                        return render(request, 'postgresql/filtros.html', {'planos': planos, 'fora_de_alcance': fora_de_alcance})
            else:
                return render(request, 'postgresql/filtros.html', {'planos': planos, 'cep_invalido': 'Cep inválido'})

    return render(request, 'postgresql/filtros.html', {'planos': planos})
    



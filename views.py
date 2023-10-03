from django.shortcuts import render

def index(request):
    return render(request, "webapp1/index.html")

def pag2(r):
    dados = {"nome": "Agnaldo Silva", "idade":240}
    return render(r,"webapp1/pagina2.html", dados)


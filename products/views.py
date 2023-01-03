from django.shortcuts import render


def index(request):
    return render(request, 'products/index.html', {'title': 'Главная страница'})

def products(request):
    return render(request, 'products/products.html', {'title': 'Продукты'})


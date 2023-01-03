from django.shortcuts import render


def index(request):
    return render(request, 'products/index.html', {'title': 'Главная страница'}) # тут и ниже title чисто для себя

def products(request):
    return render(request, 'products/products.html', {'title': 'Продукты'})


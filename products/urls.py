from django.urls import path

from products.views import products, basket_add, basket_remove

app_name = 'products'

urlpatterns = [
    path('', products, name='home'),
    path('category/<int:category_id>/', products, name='category'),
    path('page/<int:page_number>/', products, name='paginator'),
    path('bascets/add<int:product_id>/', basket_add, name='basket_add'),
    path('bascets/remove<int:basket_id>/', basket_remove, name='basket_remove'),
]


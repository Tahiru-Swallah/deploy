from django.urls import path
from .views import product_list, create_product_view, product_detail, edit_product, delete_product, product_search

app_name = 'products'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('products/<slug:category_slug>/', product_list, name='product_list_slug'),
    path('<int:id>/<slug:slug>', product_detail, name='product_detail'),
    path('post_product/', create_product_view, name='create_product'),
    path('<int:id>/<slug:slug>/edit/', edit_product, name='edit_product'),
    path('<int:id>/<slug:slug>/del/', delete_product, name='delete'),
    path('search/', product_search, name='search')
]
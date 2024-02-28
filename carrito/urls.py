from django.urls import path
from . import views

urlpatterns=[
    path('',views.inicio, name='inicio'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('galeria/', views.galeria, name='galeria'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('crud/', views.crud, name='crud' ),
    path('crear/', views.crearProducto, name='crear' ),
    path('eliminar/<id>', views.eliminar, name='eliminar'),
    path('modificar/<id>', views.modificar, name='modificar'),
    path('carrito/', views.carrito, name='carrito'),
]
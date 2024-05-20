from django.urls import path
from postgresql import views

urlpatterns = [
    path('', views.index, name='index'),
    path('comparativo', views.comparativo, name='comparativo'),
    path('sobre', views.sobre, name='sobre'),
    path('contato', views.contato, name='contato'),
    path('filtros', views.filtros, name='filtros'),


]
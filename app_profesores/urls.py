from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('<int:id>', views.listar_profesores, name='listar_profesores'),
    path('agregar/', views.agregar_profesores, name='agregar_profesores'),
    path('editar/<int:id>/', views.editar_profesores, name='editar_profesores'),
    path('borrar/<int:id>/', views.borrar_profesores, name='borrar_profesores'),
]
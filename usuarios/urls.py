from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_vendedor/', views.cadastrar_vendedor, name='cadastrar_vendedor'),
    path('login/', views.login, name='login'),
    path('sair/', views.logout, name='logout'),
    path('desativar_usuario/<str:id>', views.desativar_usuario, name='desativar_usuario')
]

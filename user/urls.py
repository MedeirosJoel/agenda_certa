# user/urls.py
from django.urls import path
from . import views  # Importa as views do mesmo diretório

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('calendario/', views.calendario, name='calendario'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('contratar-servicos/', views.contratar_servicos, name='contratar_servicos'),
    path('confirmacao/', views.confirmacao, name='confirmacao'),

]

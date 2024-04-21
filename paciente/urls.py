from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('escolher_horario/<int:id_dados_medicos>/', views.escolher_horario, name="escolher_horario"),
]
from django.urls import path 
from .views import LoginView , UsuarioListCreat, UsuarioRetrieveUpdateDestroy, ReservaAmbienteListCreate , ReservaAmbienteRetrieveUpdateDestroy, ReservaAmbienteProfessorList, DisciplinaListCreate , DisciplinaRetrieveUpdateDestroy, DisciplinaProfessorList, SalaListCreate, SalaRetrieveUpdateDestroy,SalaProfessorList

urlpatterns = [
    #Login
    path('login/', LoginView.as_view()),

    # Usuario 
    path('usuario/', UsuarioListCreat.as_view()),
    path('usuario/<int:pk>/', UsuarioRetrieveUpdateDestroy.as_view()),

    #Reserva Ambiente
    path('reservas/', ReservaAmbienteListCreate.as_view()),
    path('reservas/<int:pk>/',ReservaAmbienteRetrieveUpdateDestroy.as_view()),
    path('professor/reservas/', ReservaAmbienteProfessorList.as_view()),

    #Disciplina 
    path('disciplinas/', DisciplinaListCreate.as_view()),
    path('disciplinas/<int:pk>/', DisciplinaRetrieveUpdateDestroy.as_view()),
    path('professor/disciplinas/', DisciplinaProfessorList.as_view()),

    #Sala 
    path('sala/', SalaListCreate.as_view()),
    path('sala/<int:pk>/', SalaRetrieveUpdateDestroy.as_view()),
    path('professor/sala/', SalaProfessorList.as_view()),

]
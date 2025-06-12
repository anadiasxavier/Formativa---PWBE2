from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListCreateAPIView , RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Usuario, Disciplina, ReservaAmbiente, Sala
from .serializers import UsuarioSerializer, DisciplinaSerializer , ReservaAmbienteSerializer, LoginSerializer, SalaSerializer
from .permissions import IsGestor , IsProfessor , IsDonoOuGestor
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import ValidationError
from django.http import Http404
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

#criar e listar usuario
class UsuarioListCreat (ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsGestor]

    

# Class que ira deletar, visualizar um em expecifico  e atualixar
class UsuarioRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsGestor]
    lookup_field = 'pk' 

     #mensagem de erro quando o usuario não é encontrada
    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise NotFound(detail="Esse usuario foi não encontrada.")
        
    # mesnsagem de erro quando o usuario é excluida com sucesso
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({"O usuario foi excluída"})



# Listar Todas e criar disciplina
class DisciplinaListCreate(ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]
    
    def perform_create(self, serializer):
        nome = serializer.validated_data['nome']
        curso = serializer.validated_data['curso']
        carga_hora = serializer.validated_data['carga_hora']
        descricao = serializer.validated_data['descricao']
   

        reservas_existentes = Disciplina.objects.filter(
            nome=nome,
            curso=curso,
            carga_hora=carga_hora,
            descricao= descricao
        )

        if reservas_existentes.exists():
            raise ValidationError("Essa disciplina já existe.")

        serializer.save(professor=self.request.user)


# Class que ira deletar, visualizar um em expecifico  e atualizar Disciplina
class DisciplinaRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [IsGestor]
    lookup_field = 'pk'

        #mensagem de erro quando a disciplina não é encontrada
    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise NotFound(detail="Essa disciplina foi não encontrada.")
        
    # mesnsagem de erro quando a disciplina é excluida com sucesso
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({"A disciplina foi excluída"})


#Listar todas as salas e criar
class SalaListCreate(ListCreateAPIView):
    queryset= Sala.objects.all()
    serializer_class = SalaSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]
    
    
# Class que ira deletar, visualizar um em expecifico  e atualizar Sala
class SalaRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    permission_classes = [IsGestor]
    lookup_field = 'pk'
    #mensagem de erro quando a sala não é encontrada
    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise NotFound(detail="Essa sala foi não encontrada.")

    # mesnsagem de erro quando a sala é excluida com sucesso
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({"A sala foi excluída"})
    
#listar as salas  que o professor tem  
class SalaProfessorList(ListAPIView):
    queryset = Sala.objects.all()
    serializer_class =  SalaSerializer
    permission_class = [IsProfessor]

   

#Listar e criar  disciplinas do professor
class DisciplinaProfessorList(ListCreateAPIView):
    serializer_class = DisciplinaSerializer
    permission_classes = [IsProfessor]

    def get_queryset(self):
        return Disciplina.objects.filter(professor = self.request.user)

#Visualizar todos e criar
class ReservaAmbienteListCreate(ListCreateAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer

    #define as permissoes
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]
    
    #consulta de modo personalizado, se caso passar o id do professor 
    def get_queryset(self):
        queryset = super().get_queryset()
        professor_id = self.request.query_params.get('professor', None)
        if professor_id:
            queryset = queryset.filter(professor_id=professor_id)
        return queryset 
    
    def perform_create(self, serializer):
        data_inicio = serializer.validated_data['data_inicio']
        data_termino = serializer.validated_data['data_termino']
        sala_reserva = serializer.validated_data['sala_reserva']
        periodo = serializer.validated_data['periodo']

        reservas_existentes = ReservaAmbiente.objects.filter(
            sala_reserva=sala_reserva,
            data_inicio__lt=data_termino,
            data_termino__gt=data_inicio,
            periodo=periodo
        )

        if reservas_existentes.exists():
            raise ValidationError("Marque outro horario, esse já está em uso.")

        serializer.save(professor=self.request.user)

#Class que ira deletar, visualizar um em expecifico  e atualizar reserva de ambiente
class ReservaAmbienteRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
        queryset = ReservaAmbiente.objects.all()
        serializer_class = ReservaAmbienteSerializer
        permission_class = [IsDonoOuGestor]
        lookup_field = 'pk'

     #mensagem de erro quando a reserva de ambiente não é encontrada
        def get_object(self):
            try:
                return super().get_object()
            except Http404:
                raise NotFound(detail="Essa reserva não foi encontrada.")
        
    # mesnsagem de erro quando a disciplina é excluida com sucesso
        def destroy(self, request, *args, **kwargs):
            super().destroy(request, *args, **kwargs)
            return Response({"A reserva foi excluída"})
            
#listar a reserva de ambientes que o professor tem  
class ReservaAmbienteProfessorList (ListAPIView):
    serializer_class = ReservaAmbienteSerializer
    permission_classes = [IsProfessor]

    def get_queryset(self):
        return ReservaAmbiente.objects.filter(professor= self.request.user)

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


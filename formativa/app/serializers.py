from rest_framework import serializers
from .models import Usuario , Disciplina , ReservaAmbiente , Sala
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario 
        fields = '__all__'
        extra_kwargs = {
            'password' : {'write_only' : True}

        }

    #fazer a senha ficar criptografada
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Usuario(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    # Mensagem de erro para caso o usuario crie o usuario com dados errado
    def is_valid(self, *, raise_exception=False):
        try:
            super().is_valid(raise_exception=raise_exception)
            super().save()
        except Exception as e:
            print(e)
            raise serializers.ValidationError({"Erro ao criar o usuario, verifique os dados enviados."})
    
class DisciplinaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'
    
    # Mensagem de erro para caso o usuario crie a disciplina com dados errado
    def is_valid(self, *, raise_exception=False):
        try:
            super().is_valid(raise_exception=raise_exception)
            super().save()
        except Exception as e:
            raise serializers.ValidationError({"Erro ao criar sala, verifique os dados enviados."})


class ReservaAmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaAmbiente
        fields = '__all__'

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'
    
    # Mensagem de erro para caso o usuario crie a sala com dados errados
    def is_valid(self, *, raise_exception=False):
        try:
            super().is_valid(raise_exception=raise_exception)
            super().save()
        except Exception as e:
            raise serializers.ValidationError({"Erro ao criar sala, verifique os dados enviados."})

    
class LoginSerializer (TokenObtainPairSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

    def validate(self, attrs):
        data = super().validate(attrs)

        data['user'] = {
            'username' : self.user.username,
            'email': self.user.email,
            'tipo' : self.user.tipo
        }
        return data
    

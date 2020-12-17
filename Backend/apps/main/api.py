from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.mant.models import *
class Registro(APIView):
    def validateCedula(self, value):
        if value is not None:
        if(len(value)!=10 or not value.isdigit()):
            return False
        else:
            impares = int(value[1]) + int(value[3]) + int(value[5]) + int(value[7])
            pares = 0
            for i in range(0,9):
                if(i%2==0):
                    res = int(value[i])*2
                    if(res>=10):
                        res = res-9
                    pares = pares+res
            total = impares+pares
            dig_validador = (((total+10)//10)*10)-total
            if(dig_validador==10):
                dig_validador = 0
            if (not(int(value[0:2])>=1 and int(value[0:2])<=24 and int(value[-1])==dig_validador)):
                return False
            else:
                return True
    else:
        return False


    def post(self, request):
        nombre = request.data.get('nombre')
        apellido = request.data.get('apellido')
        identificacion = request.data.get('identificacion')
        direccion = request.data.get('direccion')
        genero = request.data.get('genero')
        ciudad = request.data.get('ciudad')
        pais = request.data.get('pais')
        if not nombre and not apellido and not identificacion and not direccion and not genero and not ciudad and not pais:
            validate = self.validateCedula(identificacion)
            if validate:
                MantPersona.objects.create(nombres=nombre,apellidos=apellido,identificacion=identificacion,direccion=direccion,genero=genero,ciudad=ciudad,pais=pais)
                
            else:
        else:


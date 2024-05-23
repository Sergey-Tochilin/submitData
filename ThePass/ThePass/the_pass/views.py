from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets

from .models import *
from .serializers import *

# Create your views here.
class PerevalViewset(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    def submitData(self, request, *args, **kwargs):
        try:
            serializer = PerevalSerializer(data=request.data)
            if serializer.is_valid():
                instance = serializer.save()
                return Response({"status": 200, "message": "Успешно отправлено", "id": instance.id})
            else:
                return Response({"status": 400, "message": "Bad Request(нехватка полей)", "id": None})
        except Exception as no_connection_to_the_db:
            return Response({"status": 500, "message": "Ошибка подключения к базе данных", "id": None})


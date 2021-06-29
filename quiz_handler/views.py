from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .serializers import PoolResultSerialazer, CreatePoolSerialazer

from .models import Pool, Choice


class GetPoolInfo(APIView):
    def post(self, request):
        value = request.data.get("id")
        query = Choice.objects.all().filter(id_poll=value)
        serializer = PoolResultSerialazer(instance=query, many=True, data={'id':int()})
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class CreatePool(APIView):
    def post(self, request):
        data = request.data
        serializer = CreatePoolSerialazer(instance=data, many=True)
        serializer.create()
        return Response(serializer.data)

'''
def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Livro
from .serializer import LivroSerializer

class LivroListView(APIView):
    def get(self, request):
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LivroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LivroDetailView(APIView):
    def get(self, request, pk):
        livro = get_object_or_404(Livro, pk=pk)
        serializer = LivroSerializer(livro)
        return Response(serializer.data)

    def delete(self, request, pk):
        livro = get_object_or_404(Livro, pk=pk)
        livro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        livro = get_object_or_404(Livro, pk=pk)
        serializer = LivroSerializer(livro, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

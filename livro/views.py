from .models import Livro
from livro import models
from .serializer import LivroSerializer

from rest_framework.viewsets import ModelViewSet

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def get_queryset(self):
        editora = self.request.query_params.get("editora")
        autor_id = self.request.query_params.get("autor_id")
        try:
            queryset = models.Livro.objects.all()

            if editora:
                queryset = queryset.filter(editora=editora)
            if autor_id:
                queryset = queryset.filter(autor_id=autor_id)
            return queryset
        except Exception as e:
            print(f"Erro ao buscar dados: {str(e)}")
            return models.Livro.objects.none()

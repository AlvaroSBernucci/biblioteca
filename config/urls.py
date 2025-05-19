from django.contrib import admin
from django.urls import path

from livro.views import LivroListView
from livro.views import LivroDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livros/',LivroListView.as_view()),
    path('livros/<int:pk>/',LivroDetailView.as_view(), name='livro-detalhe')
]

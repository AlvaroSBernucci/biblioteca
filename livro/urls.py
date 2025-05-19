from rest_framework import routers
from livro.views import LivroViewSet

router = routers.SimpleRouter()
router.register(r'', LivroViewSet, basename='livro')
urlpatterns = router.urls

from rest_framework.routers import SimpleRouter, DefaultRouter

from .views import BookViewSet, CategoryViewSet

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('categories', CategoryViewSet)
urlpatterns = router.urls
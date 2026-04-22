from rest_framework.routers import SimpleRouter, DefaultRouter

from .views import BookViewSet

router = DefaultRouter()
router.register('books', BookViewSet)
urlpatterns = router.urls
from rest_framework import routers
from .api import ProductViewSet, UserViewSet

router = routers.DefaultRouter()

router.register('api/products', ProductViewSet, 'store')
router.register('api/user', UserViewSet, 'user')

urlpatterns = router.urls
from user_management.views import MeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('me', MeViewSet, basename='me')

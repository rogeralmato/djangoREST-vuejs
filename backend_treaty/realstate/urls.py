from rest_framework import routers
from realstate.viewsets import ResidenceViewSet

router = routers.SimpleRouter()
router.register('all', ResidenceViewSet)

urlpatterns = router.urls
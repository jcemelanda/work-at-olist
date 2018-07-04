from rest_framework import routers

from core.views import CallStartRecordViewSet
from core.views import CallEndRecordViewSet

router = routers.SimpleRouter()
router.register(r'start-record', CallStartRecordViewSet)
router.register(r'end-record', CallEndRecordViewSet)

urlpatterns = router.urls
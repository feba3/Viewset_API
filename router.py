from onlineapp.viewsets import Onlineviewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('online',Onlineviewset)
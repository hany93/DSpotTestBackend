from rest_framework import routers

from profiles.views import ProfileViewSet

router = routers.DefaultRouter()
#todo Path to access the methods of profiles
router.register(r'profiles', ProfileViewSet)
urlpatterns = router.urls

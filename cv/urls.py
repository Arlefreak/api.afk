from . import views
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cv', views.CVViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

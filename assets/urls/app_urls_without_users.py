from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# Register new routes below

urlpatterns = [
    url(r'^', include(router.urls))
]

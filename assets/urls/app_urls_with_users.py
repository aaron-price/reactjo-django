from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# Register new routes below
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    url(r'^login/', views.LoginViewSet.as_view()),
    url(r'^', include(router.urls))
]

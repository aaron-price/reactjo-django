from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from courses import views

router = routers.SimpleRouter()
router.register(r'courses', views.CourseViewSet)
router.register(r'reviews', views.ReviewViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',
                                namespace='rest_framework')),
    url(r'^api/', include(router.urls, namespace='api'))
]

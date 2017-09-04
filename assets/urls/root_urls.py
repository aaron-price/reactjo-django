from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from courses import views

router = routers.SimpleRouter()
# Add views to the router here. For example:
# router.register(r'posts', views.PostViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',
                                namespace='rest_framework')),
    url(r'^api/', include(router.urls, namespace='api'))
]

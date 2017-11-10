from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='api/', permanent=True)),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls'))
]

# Add debug toolbar route
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

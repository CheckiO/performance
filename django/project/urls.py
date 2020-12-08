from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from apps.profiles.api.urls import urlpatterns as profiles_api_urlpatterns
from apps.rest_api.routers import ApiRouter


rest_api = ApiRouter()
rest_api.register(profiles_api_urlpatterns)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rest_api.urls)),
]

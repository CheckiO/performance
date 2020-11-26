from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from apps.profiles.api.urls import urlpatterns as profiles_api_urlpatterns
from apps.rest_api.routers import ApiRouter

from views import BlankPage, EmptyPage


rest_api = ApiRouter()

rest_api.register(profiles_api_urlpatterns)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rest_api.urls)),
]

# debug
urlpatterns += [
    path('blank/', BlankPage.as_view()),
    path('empty/', EmptyPage.as_view()),
]

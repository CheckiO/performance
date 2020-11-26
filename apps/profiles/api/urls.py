from apps.profiles.api import views


urlpatterns = (
    (r'current-user', views.CurrentUsersViewSet),
)

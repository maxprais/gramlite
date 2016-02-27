from django.conf.urls import url
from . import views

app_name = 'gramlite'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^check_user', views.Check_User.as_view(), name='check-user'),
    url(r'^gallery/(?P<username>\w+)/(?P<templateid>\w+)/$', views.Styles.as_view(), name='styles'),
]

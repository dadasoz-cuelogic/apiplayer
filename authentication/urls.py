from django.conf.urls import include, url

from django.conf.urls import include, url
from authentication import views

urlpatterns = [
    url(r'^$', views.login_view, name="login"),
    url(r'^logout$', views.logout_view, name="logout"),
]
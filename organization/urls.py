from django.conf.urls import include, url
from organization import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^add-api/$', views.add_api, name="add_api"),
    url(r'^endpoint/$', views.endpoint, name="endpoint"),
]

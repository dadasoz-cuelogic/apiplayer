from django.conf.urls import include, url
from organization import views

urlpatterns = [
    url(r'^', views.dashboard, name="dashboard"),
]

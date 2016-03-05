from django.conf.urls import include, url
from developer import views

urlpatterns = [
    url(r'^', views.dashboard, name="dashboard"),
]

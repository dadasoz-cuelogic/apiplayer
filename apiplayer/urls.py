from django.conf.urls import include, url
from django.contrib import admin
from apiplayer import views
from organization import urls as organization_urls
from developer import urls as developer_urls

urlpatterns = [
    url(r'^$', views.index, name="frontend"),
    url(r'^org/', include(organization_urls), name="organization"),
    url(r'^dev/', include(developer_urls), name="developer"),
    url(r'^admin/', include(admin.site.urls)),
]

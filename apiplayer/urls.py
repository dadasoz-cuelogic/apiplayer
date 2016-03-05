from django.conf.urls import include, url
from django.contrib import admin
from apiplayer import views
from organization import urls as organization_urls
from developer import urls as developer_urls
from product import urls as product_urls
from api import urls as api_urls
from reviews import urls as reviews_urls

urlpatterns = [
    url(r'^$', views.index, name="frontend"),
    url(r'^org/', include(organization_urls), name="organization"),
    url(r'^dev/', include(developer_urls), name="developer"),
    url(r'^product/', include(product_urls, namespace="product")),
    url(r'^api/', include(api_urls), name="api"),
    url(r'^reviews_urls/', include(reviews_urls), name="reviews"),
    url(r'^admin/', include(admin.site.urls)),
]

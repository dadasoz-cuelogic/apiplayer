from django.conf.urls import include, url
from api import views as api_views

urlpatterns = [
    url(r'^player/(?P<product_key>[^/]*)/$', api_views.player, name='player'),
    url(r'^get-data/', api_views.get_data, name="get_data"),
]

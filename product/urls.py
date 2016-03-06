from django.conf.urls import include, url
from product import views

urlpatterns = [
    url(r'^get-all-categories/$', views.get_all_categories,
        name="get_all_categories"),
    url(r'^add/$', views.add_product, name="add_product"),
    url(r'^view/$', views.view_product, name="view_product"),
    url(r'^edit/(?P<product_key>[^/]*)/$',
        views.edit_product, name="edit_product"),
    url(r'^endpoint/add/$', views.add_endpoint, name="add_endpoint"),
    url(r'^section/add/$', views.add_section, name="add_section"),
    url(r'^api/add/$', views.add_api, name="add_api"),
    url(r'^player/(?P<product_key>[^/]*)',
        views.dashboard_iframe, name='dev_api_url'),
]

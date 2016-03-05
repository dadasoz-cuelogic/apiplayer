from django.conf.urls import include, url
from product import views

urlpatterns = [
	url(r'^get-all-categories/$', views.get_all_categories, name="get_all_categories"),
    url(r'^add/$', views.add_product, name="add_product"),
    url(r'^view/$', views.view_product, name="view_product"),
    url(r'^view/(?P<product_key>[^/]*)', views.dashboard_iframe, name='dev_api_url'),
    url(r'^player/(?P<product_key>[^/]*)', views.dashboard_iframe, name='dev_api_url'),
    url(r'^edit/(?P<product_key>[^/]*)', views.edit_product, name='edit_product'),
]

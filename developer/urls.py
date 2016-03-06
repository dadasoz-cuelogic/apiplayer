from django.conf.urls import include, url
from developer import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^categories', views.get_all_categories, name='all_categories'),
    url(r'^products-category', views.get_all_products_in_category, name='all_products_category'),
    url(r'^all-products-category', views.get_all_products, name='all_products'),
    url(r'^dev-api/(?P<product_key>[^/]*)', views.dashboard_iframe, name='dev_api_url'),
]

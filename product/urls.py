from django.conf.urls import include, url
from product import views

urlpatterns = [
	url(r'^get-all-categories/$', views.get_all_categories, name="get_all_categories"),
    url(r'^add-product/$', views.add_product, name="add_product"),
]

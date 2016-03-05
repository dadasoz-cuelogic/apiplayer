from django.conf.urls import include, url
from developer import views

urlpatterns = [
    url(r'^', views.dashboard, name="dashboard"),
    url(r'^categories', views.get_all_categories, name='all_categories'),
    url(r'^products-category', views.get_all_products_in_category, name='all_products_category'),
]

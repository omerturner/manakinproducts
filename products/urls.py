from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.show_products, name='products'),
    url(r'(?P<pk>\d+)/$', views.product_detail, name='detail'),
]
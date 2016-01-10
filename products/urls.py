from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.show_products, name='products'),
    url(r'(?P<slug>[-\w]+)/$', views.product_detail, name='detail'),
]
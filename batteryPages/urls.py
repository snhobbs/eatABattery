from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^Healthy_Living', views.healthyLiving),
    url(r'^PJ', views.pj),
    url(r'^Kirkland_Corner', views.poems),
    url(r'^Bear', views.bear),
    ]

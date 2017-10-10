from django.conf.urls import url
from getpost.sites import views

urlpatterns = [
    url(r'^(/(?P<id>\d+))?$', views.main_view, name='main_view'),
]

from django.conf.urls import url
from sites import views

urlpatterns = [
    url(r'^(?P<id>\d+)?$', views.get_request, name='main_view'),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$|^index$', views.index, name='index'),
    url(r'^cows$', views.cows, name='cows'),
    url(r'^no_page$', views.no_page, name='no_page')
]


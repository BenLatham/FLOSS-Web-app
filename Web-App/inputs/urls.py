from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<page>((intro)|(financial)|(assets)|(land)|(dairy)|(cropping)|(forage)|(summary)))?$', views.inputs, name='inputs'),
    url(r'^test$', views.formset_test, name='test')
]




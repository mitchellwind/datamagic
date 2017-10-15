from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^highcharts', views.highcharts, name='highcharts'),
    url(r'^d3', views.d3, name='d3'),
    url(r'^plotly', views.plotly, name='plotly'),
    url(r'^list_query', views.list_query, name='list_query'),
    url(r'^data_query', views.data_query, name='data_query')
]
from django.conf.urls import patterns, url
from app_hcare import views

urlpatterns = patterns('',
    url('^$', views.main, name='main'),
    url('process_data$', views.process_data, name='process_data'),
)
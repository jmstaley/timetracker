from django.conf.urls.defaults import *

urlpatterns = patterns('timetracker.views',
                      (r'^dashboard/', 'dashboard'),
                      (r'', 'index'),)

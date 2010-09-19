from django.conf.urls.defaults import *

urlpatterns = patterns('timetracker.views',
                      (r'^dashboard', 'dashboard'),
                      (r'^task/detail/(?P<task_id>\d{1})', 'task_detail'),
                      (r'', 'index'),)

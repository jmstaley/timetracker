from django.conf.urls.defaults import *

urlpatterns = patterns('timetracker.views',
                      url(r'^dashboard', 'dashboard', name='dashboard'),
                      url(r'^task/detail/(?P<task_id>\d{1})', 
                          'task_detail', 
                          name='task_detail'),
                      url(r'', 'index', name='tracker_index'),)

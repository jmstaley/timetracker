from django.conf.urls.defaults import *

urlpatterns = patterns('timetracker.views',
                      url(r'^dashboard', 'dashboard', name='dashboard'),
                      url(r'^task/detail/(?P<task_id>\d{1})/add', 
                          'add_work',
                          name='add_work'),
                      url(r'^task/detail/(?P<task_id>\d{1})', 
                          'task_detail', 
                          name='task_detail'),
                      url(r'^task/add', 'add_task', name='add_task'),
                      url(r'', 'index', name='tracker_index'),)

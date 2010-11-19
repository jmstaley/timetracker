from django.conf.urls.defaults import *

urlpatterns = patterns('timetracker.views',
                      url(r'^dashboard', 'dashboard', name='dashboard'),
                      url(r'^task/detail/(?P<task_id>\d+)/add', 
                          'add_work',
                          name='add_work'),
                      url(r'^task/(?P<task_id>\d+)/(?P<work_id>\d+)/',
                          'edit_work',
                          name='edit_work'),
                      url(r'^task/detail/(?P<task_id>\d+)/$', 
                          'task_detail', 
                          name='task_detail'),
                      url(r'^task/detail/(?P<task_id>\d+)/remove',
                          'remove_task',
                          name='remove_task'),
                      url(r'^task/add', 'add_task', name='add_task'),
                      url(r'', 'index', name='tracker_index'),)

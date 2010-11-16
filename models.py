import time
from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """ Simple task for tracking time worked """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User)
    due_date = models.DateField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=True)
    uid = models.IntegerField()
    
    def __unicode__(self):
        return u'%s' % self.title

    def save(self, force_insert=False, force_update=False):
        current_tasks = Task.objects.filter(author__id=self.author.id)
        self.uid = len(current_tasks)+1
        super(Task, self).save(force_insert, force_update)

    @property
    def total_time_worked(self):
        work = self.work()
        total_time = 0
        for w in work:
            total_time += w.duration
        return str(timedelta(seconds=total_time))

    def work(self):
        work = Work.objects.filter(task=self)
        return work

    @models.permalink
    def get_absolute_url(self):
        return ('task_detail', [], {'task_id': self.uid})

class Work(models.Model):
    """ Work to be attached to a task """
    description = models.TextField(blank=True)
    date = models.DateField()
    duration = models.IntegerField(blank=True)
    task = models.ForeignKey(Task)
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=True)
    tid = models.IntegerField()

    def save(self, force_insert=False, force_update=False):
        current_work = Work.objects.filter(task__id=self.task.id)
        self.tid = len(current_work)+1
        super(Work, self).save(force_insert, force_update)
    
    def __unicode__(self):
        return u'%s %s' % (self.task.title, self.date)

    @property
    def length(self):
        return str(timedelta(seconds=self.duration))

import time
from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import User

from managers import FinishedTaskManager, OpenTaskManager

class Task(models.Model):
    """ Simple task for tracking time worked """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User)
    due_date = models.DateField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=True)
    uid = models.IntegerField()
    completed = models.BooleanField(blank=True, default=False)

    # set managers
    finished = FinishedTaskManager()
    open = OpenTaskManager()
    objects = models.Manager()
    
    def __unicode__(self):
        return u'%s' % self.title

    def save(self, force_insert=False, force_update=False):
        last = Task.objects.filter(author__id=self.author.id).order_by('uid').reverse()[:1]
        if last:
            self.uid = last[0].uid+1
        else:
            self.uid = 1
        super(Task, self).save(force_insert, force_update)

    def complete(self):
        self.completed = True
        super(Task, self).save()

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
        return ('task_detail', [], {'task_id': self.id})

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

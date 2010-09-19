import time
from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """ Simple task for tracking time worked """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User)
    
    def __unicode__(self):
        return u'%s' % self.title

    def total_time_worked(self):
        work = self.work()
        total_time = timedelta()
        for w in work:
            total_time += w.duration
        return total_time

    def work(self):
        work = Work.objects.filter(task=self)
        return work

class Work(models.Model):
    """ Work to be attached to a task """
    description = models.TextField(blank=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    task = models.ForeignKey(Task)
    
    def __unicode__(self):
        return u'%s %s' % (self.task.title, self.date)

    @property
    def duration(self):
        end_dt = datetime.combine(self.date, self.end_time)
        start_dt = datetime.combine(self.date, self.start_time)
        return end_dt - start_dt

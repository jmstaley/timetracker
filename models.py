from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """ Simple task for tracking time worked """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User)
    
    def __unicode__(self):
        return u'%s' % self.title

class Work(models.Model):
    """ Work to be attached to a task """
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    task = models.ForeignKey(Task)
    
    def __unicode__(self):
        return u'%s %s' % (self.task.title, self.date)

    @property
    def duration(self):
        return end_time - start_time

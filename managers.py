from django.db import models

class FinishedTaskManager(models.Manager):
    def get_query_set(self):
        return super(CompletedTaskManager, self).get_query_set().filter(
            completed=True)

class OpenTaskManager(models.Manager):
    def get_query_set(self):
        return super(OpenTaskManager, self).get_query_set().filter(
            completed=False)

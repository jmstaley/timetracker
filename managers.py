from django.db import models

class FinishedTaskManager(models.Manager):
    def get_query_set(self):
        return super(FinishedTaskManager, self).get_query_set().filter(
            status=self.model.FINISHED)

class OpenTaskManager(models.Manager):
    def get_query_set(self):
        return super(OpenTaskManager, self).get_query_set().filter(
            status=self.model.OPEN)

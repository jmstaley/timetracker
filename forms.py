from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget

from models import Task, Work
from fields import DurationField

class AddTaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ('author', 'uid')
        widgets = {'due_date': SelectDateWidget()}

class AddWorkForm(ModelForm):
    duration = DurationField()

    class Meta:
        model = Work
        exclude = ('task', 'tid', 'hour', 'minute')
        widgets = {'date': SelectDateWidget()}

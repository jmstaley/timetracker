from django.forms import ModelForm
from django.forms.widgets import TextInput
from django.forms.extras.widgets import SelectDateWidget

from models import Task, Work
from fields import DurationField

class AddTaskShortcut(ModelForm):
    class Meta:
        model = Task
        exclude = ('author', 'uid', 'status')
        widgets = {'due_date': SelectDateWidget(),
                   'description': TextInput()}

class AddTaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ('author', 'uid', 'status')
        widgets = {'due_date': SelectDateWidget(),
                   'description': TextInput()}

class AddWorkForm(ModelForm):
    duration = DurationField()
    class Meta:
        model = Work
        exclude = ('task', 'tid')
        widgets = {'date': SelectDateWidget(),
                   'description': TextInput()}

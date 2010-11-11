from django.forms import ModelForm
from django.forms.widgets import TextInput
from django.forms.extras.widgets import SelectDateWidget

from models import Task, Work

class AddTaskShortcut(ModelForm):
    class Meta:
        model = Task
        exclude = ('author', 'uid')
        widgets = {'due_date': SelectDateWidget(),
                   'description': TextInput()}

class AddTaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ('author', 'uid')
        widgets = {'due_date': SelectDateWidget()}

class AddWorkForm(ModelForm):
    class Meta:
        model = Work
        exclude = ('task', 'tid')
        widgets = {'date': SelectDateWidget()}

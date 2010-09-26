from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget

from models import Task, Work

class AddTaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ('author',)
        widgets = {'due_date': SelectDateWidget()}

class AddWorkForm(ModelForm):
    class Meta:
        model = Work
        exclude = ('task', )
        widgets = {'date': SelectDateWidget(),}

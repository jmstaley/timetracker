from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from models import Task
from forms import AddTaskForm, AddWorkForm

def index(request):
    return render_to_response('timetracker/index.html',
                              context_instance = RequestContext(request))

@login_required
def dashboard(request):
    tasks = Task.objects.filter(author__id=request.user.id)
    return render_to_response('timetracker/dashboard.html',
                              {'tasks': tasks},
                              context_instance = RequestContext(request))

@login_required
def task_detail(request, task_id):
    task = Task.objects.get(uid=task_id, author__id=request.user.id)
    return render_to_response('timetracker/task_detail.html', 
                              {'task': task},
                              context_instance = RequestContext(request))

@login_required
def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(data=request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.author = request.user
            new_task.save()
            return HttpResponseRedirect(new_task.get_absolute_url())
    else:
        form = AddTaskForm()
        return render_to_response('timetracker/add_task.html',
                                  {'form': form},
                                  context_instance = RequestContext(request))

@login_required
def add_work(request, task_id):
    if request.method == 'POST':
        form = AddWorkForm(data=request.POST)
        if form.is_valid():
            new_work = form.save(commit=False)
            task = Task.objects.get(uid=task_id, author__id=request.user.id)
            new_work.task = task
            new_work.save()
            return HttpResponseRedirect(task.get_absolute_url())
    else:
        form = AddWorkForm()
        return render_to_response('timetracker/add_work.html',
                                  {'form': form},
                                  context_instance = RequestContext(request))

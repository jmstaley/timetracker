from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect

from models import Task, Work
from forms import AddTaskForm, AddWorkForm, AddTaskShortcut

def index(request):
    return render_to_response('timetracker/index.html',
                              context_instance = RequestContext(request))

@csrf_protect
@login_required
def dashboard(request, filter=''):
    if request.method == 'POST':
        form = AddTaskShortcut(data=request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.author = request.user
            new_task.save()

    form = AddTaskShortcut()
    if filter == 'finished':
        tasks = Task.finished.filter(author__id=request.user.id).order_by('due_date')
    else:
        tasks = Task.live.filter(author__id=request.user.id).order_by('due_date')
    return render_to_response('timetracker/dashboard.html',
                              {'tasks': tasks,
                               'form': form},
                              context_instance = RequestContext(request))

@csrf_protect
@login_required
def task_detail(request, task_id):
    if request.method == 'POST':
        form = AddWorkForm(data=request.POST)
        if form.is_valid():
            new_work = form.save(commit=False)
            task = Task.objects.get(id=task_id, author__id=request.user.id)
            new_work.task = task
            new_work.save()
    else:
        form = AddWorkForm()

    task = Task.objects.get(id=task_id, author__id=request.user.id)
    return render_to_response('timetracker/task_detail.html', 
                              {'task': task,
                               'form': form},
                              context_instance = RequestContext(request))

@csrf_protect
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

@csrf_protect
@login_required
def add_work(request, task_id):
    if request.method == 'POST':
        form = AddWorkForm(data=request.POST)
        if form.is_valid():
            new_work = form.save(commit=False)
            task = Task.objects.get(id=task_id, author__id=request.user.id)
            new_work.task = task
            new_work.save()
            return HttpResponseRedirect(task.get_absolute_url())
    else:
        form = AddWorkForm()
    return render_to_response('timetracker/add_work.html',
                              {'form': form},
                              context_instance = RequestContext(request))

@csrf_protect
@login_required
def edit_work(request, task_id, work_id):
    work = Work.objects.get(id=work_id, task__id=task_id)
    hours, minutes = work.length.split(':')[:2]
    data = {'description': work.description,
            'date': work.date,
            'duration_0': hours,
            'duration_1': minutes}
    form = AddWorkForm(data)
    return render_to_response('timetracker/add_work.html',
                              {'form': form},
                              context_instance = RequestContext(request))

@login_required
def remove_task(request, task_id):
    t = Task.objects.get(id=task_id)
    t.delete()
    return HttpResponseRedirect(reverse('dashboard'))

@login_required
def complete_task(request, task_id):
    t = Task.objects.get(id=task_id)
    t.complete()
    return HttpResponseRedirect(reverse('dashboard'))


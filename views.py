from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from models import Task, Work

def index(request):
    return render_to_response('timetracker/index.html')

@login_required
def dashboard(request):
    tasks = Task.objects.filter(author__id=request.user.id)
    return render_to_response('timetracker/dashboard.html',
                              {'tasks': tasks})

@login_required
def task_detail(request, task_id):
    task = Task.objects.get(id=task_id, author__id=request.user.id)
    return render_to_response('timetracker/task_detail.html', 
                              {'task': task})

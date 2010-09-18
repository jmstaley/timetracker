from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from models import Task, Work

def index(request):
    return render_to_response('timetracker/index.html')

@login_required
def dashboard(request):
    return render_to_response('timetracker/dashboard.html')

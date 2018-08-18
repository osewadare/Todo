from django.shortcuts import render, HttpResponse
import json
from .models import Task
from .forms import TaskForm

def home(request):
    tasks = Task.objects.all()
    submitted = False
    if request.method =='POST':
        taskform = TaskForm(request.POST)
        if taskform.is_valid():
            taskform.save()
            submitted = True
    elif request.method=='GET':
        taskform = TaskForm()
    context = {'submitted': submitted,'tasks': tasks, 'taskform' : taskform}
    return render(request, 'tasks/index.html', context)


def createtask(request):

    # Check if request is POST
    if request.method =='POST':

        #Get form data from request object
        title = request.POST.get('title')
        description = request.POST.get('description')

        #Create empty dictionary to store response data
        response_data={}

        #Save form data to database
        task = Task(title=title, description=description)
        task.save()

        #Save new object data to dictionary
        response_data['title'] = task.title
        response_data['description'] = task.description

        return HttpResponse(json.dumps(response_data), content_type="application/json")

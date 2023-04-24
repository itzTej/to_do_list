from django.shortcuts import render,HttpResponse
from home.models import Task
# Create your views here.
def home(request):
    context = {'success':False, 'name':'Tej'}
    if request.method == "POST":
        # Handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        print(title,desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success':True}
    return render(request,'index.html',context)

def tasks(request):
    # Fetch all the tasks
    allTasks = Task.objects.all()
    context = {'tasks':allTasks}
    return render(request,'about.html',context)

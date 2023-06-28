from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from todoapp.models import Task
from . form import TaskForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.
def index(request):
    return render(request, "index.html")

class Taskview(ListView):
    model = Task
    template_name = 'add.html'
    context_object_name = 'task'

class TaskDetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class TaskUpdate(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields =('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('todo:cvdetail',kwargs={'pk':self.object.id})

class TaskDelete(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('todo:cvhome')
def add(request):
    obj = Task.objects.all()
    if request.method=='POST':
        tname=request.POST.get('tname','')
        prio=request.POST.get('prio','')
        date=request.POST.get('date','')
        task=Task(name=tname, priority=prio,date=date)
        task.save()
        # return redirect('/')
    return render(request,"add.html",{'task': obj})
def delete(request,task_id):
    task = Task.objects.get(id=task_id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{'task': task})

def update(request,task_id):
    task=Task.objects.get(id=task_id)
    form=TaskForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html',{'form':form,'task':task})
from django.shortcuts import render,redirect
from . models import Todo
from . forms import TodoForm

def index(request):
    form=TodoForm()
    todo=Todo.objects.all()
    context={
        "form":form,
        "todo":todo
    }
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"index.html",context)    
    return render(request,"index.html",context)
def delete(request,id):
    todo=Todo.objects.get(id=id)
    if request.method=="POST":
        todo.delete()
        return redirect("home")
def update(request,id):
    todo=Todo.objects.get(id=id)
    form=TodoForm()
    if request.method=='POST':
        form=TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request,"update.html",{"form":form})
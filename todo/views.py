from django.shortcuts import render,redirect,get_object_or_404
from .models import Todo
# Create your views here.
def todo_lis(request):
    todos=Todo.objects.all()
    return render(request,'todo/index.html',{'todos':todos})

def create_todo(request):
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        Todo.objects.create(title=title,description=description)
    return redirect('todo_lis')


def delete_todo(request,id):
    todo=get_object_or_404(Todo,id=id)
    todo.delete()
    return redirect('todo_lis')
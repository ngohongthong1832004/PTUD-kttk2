from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    return render(request, 'index.html')



def todo(request):
    todo = Todo.objects.all()
    
    print(todo)
    return render(request, 'todo.html', {'todo': todo})

def add_todo (request):
    if request.method == 'POST':
        title = request.POST['title']
        todo = Todo(title=title)
        todo.save()
        todo = Todo.objects.all()
        return render(request, 'todo.html', {'todo': todo})
    else:
        return render(request, 'todo.html', {'todo': todo})

def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    todo = Todo.objects.all()
    return render(request, 'todo.html', {'todo': todo})
    

def cv(request):
    cv = CV.objects.last()
    print(cv)
    return render(request, 'cv.html', {'cv': cv})



def update_cv(request):
    cv = CV.objects.all()
    if request.method == 'POST':        
        name = request.POST['name']
        email = request.POST['email']
        education = request.POST['education']
        work_experience = request.POST['work_experience']
        skill = request.POST['skill']
        cv = CV(name=name, email=email, education=education, work_experience=work_experience, skill=skill)
        cv.save()
        return render(request, 'cv.html', {'cv': cv})
    else:
        return render(request, 'update_cv.html', {'cv': cv})
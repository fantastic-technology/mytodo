from django.shortcuts import render, redirect, get_object_or_404
from .models import Create
from django.contrib.auth.models import User, auth
from django.contrib import messages
# from django.contrib.allauth.info.passage.*args.*args, **kwargs, user info git init fo
from django.contrib.auth.decorators import login_required
# Create your views here.
def landing(request):
    return render(request, 'landing.html')
@login_required(login_url='signin')
def home(request):
    todos = Create.objects.all()
    return render(request, 'base.html', {"todos": todos})
def todo(request, id):
    todo_obj = get_object_or_404(Create, pk=id)
    tasktitle = todo_obj.title
    taskdescription = todo_obj.description
    dd = todo_obj.due_date
    return render(request, 'todo.html', {"tasktitle": tasktitle, "td": taskdescription, "dd":dd})
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter( username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('login')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                return redirect('todohome')
        else:
            messages.info(request, "Password not Matched")
            return redirect('signup')
    else:
        return render(request, "signup.html")
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password'] 

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('todohome')
        else:
            messages.info(request, 'Crredentials Invalid')
            return redirect("signin")
    else:
        return render(request, "signin.html")
def logout(request):
    auth.logout(request)
    return redirect('signin')     
@login_required(login_url='signin')       
def create(request):
    if request.method == "POST":
        createform = Create()
        user = request.user.username
        title = request.POST['title']
        description = request.POST['description']
        duedate = request.POST['due-date']
        createform.user = user
        createform.title = title
        createform.description = description
        createform.due_date = duedate
        createform.save()
        return redirect('todohome')
    else:
        return render(request, 'create.html')
def completed(request):
    completed_todo = Create.objects.filter(completed=True)
    return render(request, 'completed.html', {"completed_todo": completed_todo})
def delete_todo(request, id):
    todo = get_object_or_404(Create, id=id)
    todo.delete()
    return redirect('todohome')
def toggle_todo_completed(request, id):
    todo = get_object_or_404(Create, id=id)
    todo.completed = not todo.completed 
    todo.save() 
    return redirect('todohome')
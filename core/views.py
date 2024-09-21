from django.shortcuts import render, redirect, get_object_or_404
from .models import Create, Contact
from django.contrib.auth.models import User, auth
from django.contrib import messages
# from django.contrib.allauth.info.passage.*args.*args, **kwargs, user info git init fo
from django.contrib.auth.decorators import login_required
# Create your views here.
def landing(request):
    return render(request, 'landing.html')
@login_required(login_url='signin')
def home(request):
    todos = Create.objects.filter(user=request.user)
    todos_len = len(todos)
    completed_todo = Create.objects.filter(completed=True, user=request.user)
    comp_todo_len = len(completed_todo)
    progress = "0%"
    if  todos_len == comp_todo_len:
        progress = "100%"
    elif comp_todo_len == 1:
        progress = "25%"    
    elif comp_todo_len == todos_len//2:
        progress = "50%"        
    elif comp_todo_len *3:  
        progress = "75%"               
    if todos_len == 0 and comp_todo_len == 0:
        progress = "0%"
    return render(request, 'base.html', {"todos": todos, "todos_len": todos_len, "comp_todo_len": comp_todo_len, "progress": progress})
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
    completed_todo = Create.objects.filter(completed=True, user=request.user)
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
def contactus(request):
    if request.method == "POST":
        contactform = Contact()
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contactform.name = name
        contactform.email = email
        contactform.subject = subject
        contactform.message = message
        contactform.save()
        messages.info(request, "Thanks for contacting us, we'll get back to you")
    return render(request, "contactus.html")    
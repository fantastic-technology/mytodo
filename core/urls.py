from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('todohome/', views.home, name='todohome'),
    path('', views.landing, name='landing'),
    path('contact-us/', views.contactus, name='contactus'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('create/', views.create, name='create'),
    path('todo/<int:id>/', views.todo, name='todo'),
    path('completed/', views.completed, name='completed'),
    path('logout/', views.logout, name='logout'),
    path('delete-todo/<int:id>/', views.delete_todo, name='delete_todo'),
    path('toggle-completed/<int:id>/', views.toggle_todo_completed, name='toggle_todo_completed'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

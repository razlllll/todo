from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('index/', views.index, name='index'),
    path('add/', views.add_todo, name='add_todo'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('complete/<int:todo_id>/', views.complete_todo, name='complete_todo'),
    path('edit/<int:todo_id>/', views.edit_todo, name='edit_todo'),
    path('api/students/', views.StudentListCreate.as_view(), name='student-list-create'),
    path('api/students/<int:pk>/', views.StudentDetail.as_view(), name='student-detail'),
    path('api/todos/', views.TodoListCreate.as_view(), name='todo-list-create'),
    path('api/todos/<int:pk>/', views.TodoDetail.as_view(), name='todo-detail'),
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', login_required(views.dashboard, login_url='login'), name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
]

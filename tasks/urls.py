from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('tasks/', views.tasklist_view, name='task_list'),
    path('profile/', views.profile_view, name='profile'),
    path('tasks/create/', views.create_task_view, name='create_task'),
    path('tasks/<int:pk>/toggle/', views.toggle_task_view, name='toggle_task'),
    path('tasks/<int:pk>/edit/', views.edit_task_view, name='edit_task'),
    path('tasks/<int:pk>/delete/', views.delete_task_view, name='delete_task'),
    path('tasks/<int:task_id>/category/<int:category_id>/add/', views.assign_category_to_task, name='assign_category'),
    path('tasks/<int:task_id>/category/<int:category_id>/remove/', views.remove_category_from_task, name='remove_category'),
    path('category/<int:category_id>/', views.tasks_by_category, name='tasks_by_category'),
]
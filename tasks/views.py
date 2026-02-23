from django.shortcuts import redirect, render
from django.db.models import Max
from django.db import models
from .forms import RegisterForm, LoginForm, TaskForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task, Category, TaskCategory


# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
            
    else:
            form = RegisterForm()
        
    return render(request, 'tasks/register.html', {'form': form})    

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('task_list')
            else:
                form.add_error(None, 'Invalid Username or Password')
        else:
            form = LoginForm()
            
    return render(request, 'tasks/login.html', {'form': LoginForm()})

@login_required
def tasklist_view(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    categories = Category.objects.all()  # ← Add this
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'all_categories': categories  # ← Pass it
    })

@login_required
def create_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def update_task_view(request, pk):
    task = Task.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def toggle_task_view(request, pk):
    task = Task.objects.get(pk=pk, user=request.user)
    task.is_completed = not task.is_completed
    task.save()
    status = "completed" if task.is_completed else "marked incomplete"
    messages.success(request, f'Task {status}!')
    return redirect('task_list')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def delete_task_view(request, pk):
    task = Task.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('task_list')
    return render(request, 'tasks/confirm_delete.html', {'task': task})

@login_required
def edit_task_view(request, pk):
    task = Task.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def assign_category_to_task(request, task_id, category_id):
    """Assign a category to a task"""
    if request.method == 'POST':
        task = Task.objects.get(id=task_id, user=request.user)
        category = Category.objects.get(id=category_id)
        
        # Check if already assigned
        if not task.category.filter(id=category_id).exists():
            # Get the highest order number and add 1
            max_order = TaskCategory.objects.filter(task=task).aggregate(
                Max('order')
            )['order__max'] or 0
            
            TaskCategory.objects.create(
                task=task,
                category=category,
                order=max_order + 1
            )
            messages.success(request, f'Added {category.name} to task')
        else:
            messages.info(request, f'{category.name} already assigned')
        
        return redirect('task_list')
    
@login_required
def remove_category_from_task(request, task_id, category_id):
    """Remove a category from a task"""
    if request.method == 'POST':
        task = Task.objects.get(id=task_id, user=request.user)
        
        TaskCategory.objects.filter(task=task, category_id=category_id).delete()
        messages.success(request, 'Category removed from task')
        
        return redirect('task_list')
@login_required
def tasks_by_category(request, category_id):
    """Show all tasks in a specific category"""
    category = Category.objects.get(id=category_id)
    
    # Get tasks for this user that have this category
    tasks = Task.objects.filter(
        user=request.user,
        categories=category
    ).order_by('-created_at')
    
    return render(
        request, 
        'tasks/task_list.html', 
        {'tasks': tasks, 'category': category}
    )    
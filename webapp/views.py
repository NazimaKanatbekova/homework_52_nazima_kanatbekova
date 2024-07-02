from django.http import HttpResponse
from django.shortcuts import render, redirect

from webapp.models import Task

def index(request):
    tasks = Task.objects.order_by('-date')
    return render(request, 'index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        date = request.POST.get('date')

        if description and status:
            task = Task(description=description, status=status, date=date)
            task.save()
            return redirect('index')  # Используем правильное имя URL-шаблона для списка задач
        else:
            return HttpResponse('Не удалось добавить задачу. Проверьте введенные данные.')

    return render(request, 'add_task.html')

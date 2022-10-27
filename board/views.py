from django.shortcuts import render
from home.models import *
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect

def template_name():
    return 'board/index.html'

def board_task_list(request, u_id, w_id, b_id):
    form = UploadFileForm(request.POST, request.FILES)
    brd = board.objects.get(id=b_id)
    tsk= brd.tasks.all()

    context = {
        'tasks_list': tsk,
        'upload': form,
        'user': user.objects.get(id=u_id),
        'workspace': workspace.objects.get(id=w_id),
        'board': brd,
    }
    return render(request, 'board/base.html', context=context)


def add_task(request, u_id, w_id, b_id):
    current_board = board.objects.get(id=b_id)
    task_count = current_board.tasks.filter(state='1').count()
    description = request.POST.get('task_description')

    current_board.tasks.create(name=request.POST.get('task_name'), description=description, order=(task_count + 1), state="1", file=" ")



    form = UploadFileForm(request.POST, request.FILES)
    context = {
        'tasks_list': board.objects.get(id=b_id).tasks.all(),
        'upload': form,
        'user': user.objects.get(id=u_id),
        'workspace': workspace.objects.get(id=w_id),
        'board': current_board,
    }
    return render(request, template_name(), context=context)


def sort_first(request,  u_id, w_id, b_id):
    form = UploadFileForm(request.POST, request.FILES)
    tasks_in_form = request.POST.getlist("item")
    tasks_list = []
    for idx, el_id in enumerate(tasks_in_form, start = 1):
        tsk = board.objects.get(id = b_id).tasks.get(id=el_id)
        tsk.order = idx
        if tsk.state != 1:
            tsk.state = 1
        tsk.save()
        tasks_list.append(tsk)



    context = {
        'tasks_list': board.objects.get(id=b_id).tasks.all(),
        'upload': form,
        'user': user.objects.get(id=u_id),
        'workspace': workspace.objects.get(id=w_id),
        'board': board.objects.get(id=b_id),
    }
    return render(request, template_name(), context=context)

def sort_second(request, u_id, w_id, b_id):
    form = UploadFileForm(request.POST, request.FILES)
    tasks_in_form = request.POST.getlist("item")
    tasks_list = []
    for idx, el_id in enumerate(tasks_in_form, start = 1):
        tsk = board.objects.get(id = b_id).tasks.get(id=el_id)
        tsk.order = idx
        if tsk.state != 2:
            tsk.state = 2
        tsk.save()
        tasks_list.append(tsk)



    context = {
        'tasks_list': board.objects.get(id=b_id).tasks.all(),
        'upload': form,
        'user': user.objects.get(id=u_id),
        'workspace': workspace.objects.get(id=w_id),
        'board': board.objects.get(id=b_id),
    }
    return render(request, template_name(), context=context)

def sort_third(request, u_id, w_id, b_id):
    form = UploadFileForm(request.POST, request.FILES)
    tasks_in_form = request.POST.getlist("item")
    tasks_list = []
    for idx, el_id in enumerate(tasks_in_form, start = 1):
        tsk = board.objects.get(id = b_id).tasks.get(id=el_id)
        tsk.order = idx
        if tsk.state != 3:
            tsk.state = 3
        tsk.save()
        tasks_list.append(tsk)



    context = {
        'tasks_list': board.objects.get(id=b_id).tasks.all(),
        'upload': form,
        'user': user.objects.get(id=u_id),
        'workspace': workspace.objects.get(id=w_id),
        'board': board.objects.get(id=b_id),
    }
    return render(request, template_name(), context=context)


def delete_task(request, pk, u_id, w_id, b_id):
    form = UploadFileForm(request.POST, request.FILES)
    board.objects.get(id = b_id).tasks.get(pk=pk).delete()



    context = {
        'tasks_list': board.objects.get(id=b_id).tasks.all(),
        'upload': form,
        'user': user.objects.get(id=u_id),
        'workspace': workspace.objects.get(id=w_id),
        'board': board.objects.get(id=b_id),
    }
    return render(request, template_name(), context=context)


def change_task(request, u_id, w_id, b_id):

    form = UploadFileForm(request.POST, request.FILES)
    task_to_change = board.objects.get(id = b_id).tasks.get(id=request.POST.get("task_to_change_id"))
    task_to_change.name = request.POST.get("task_name")
    task_to_change.description = request.POST.get("task_description")
    task_to_change.save()



    context = {
        'tasks_list': board.objects.get(id=b_id).tasks.all(),
        'upload': form,
        'user': user.objects.get(id=u_id),
        'workspace': workspace.objects.get(id=w_id),
        'board': board.objects.get(id=b_id),
    }
    return render(request, template_name(), context=context)


def add_file(request, u_id, w_id, b_id):
    task_to_change = board.objects.get(id = b_id).tasks.get(id=request.POST.get("task_to_change_id"))
    file = request.FILES['file']
    if task_to_change.file != ' ':
        task_to_change.file.delete()
    task_to_change.file = file
    task_to_change.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_file(request, pk, u_id, w_id, b_id):
    form = UploadFileForm(request.POST, request.FILES)
    task_to_change = board.objects.get(id = b_id).tasks.get(pk=pk)
    task_to_change.file.delete()
    task_to_change.file = ' '
    task_to_change.save()


    context = {
        'tasks_list': board.objects.get(id=b_id).tasks.all(),
        'upload': form,
        'user': user.objects.get(id=u_id),
        'workspace': workspace.objects.get(id=w_id),
        'board': board.objects.get(id=b_id),
    }
    return render(request, template_name(), context=context)



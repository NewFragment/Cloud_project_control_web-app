from django.shortcuts import render, redirect
from home.models import *


def workspace_main(request, u_id, w_id):
    print(w_id)
    print(id)
    usr = user.objects.get(id=u_id)
    wspace = workspace.objects.get(id = w_id)
    print(wspace.id)
    not_added_usrs = user.objects.exclude(w_usrs__pk=w_id)
    if request.method == "POST":
        print(request.POST)
        if request.POST.get("add_workspace"):
            bn = request.POST.get("board_name")
            bd = request.POST.get("board_description")
            b = wspace.board_set.create(name=bn, description=bd)
        if request.POST.get("add_user"):
            for el in not_added_usrs:
                if request.POST.get(str(el.pk)) == 'on':
                    el.w_usrs.add(wspace)
                    p = user.objects.get(name=el.name).workspace_permissions_set.get(
                        workspace_id=wspace.pk)
                    p.is_creator = False
                    p.permission_change_workspace = False
                    p.permission_delete_workspace = False
                    p.permission_delete_user = False
                    p.save()
        if request.POST.get("user_to_delete"):
            p = user.objects.get(name = request.POST.get("user_to_delete")).workspace_permissions_set.filter(workspace_id = wspace.pk)
            p.delete()


    template_name = 'workspace/base.html'
    context = {
        'user': usr,
        'work_space': wspace,
        'boards': workspace.objects.get(id = w_id).board_set.all(),
        'added_usrs': user.objects.filter(w_usrs__pk=w_id),
        'permissions_list': workspace_permissions.objects.filter(workspace_id=wspace),
        'not_added_usrs': not_added_usrs,
    }
    return render(request, template_name, context=context)


def workspace_change(request, u_id, w_id):
    wspace = workspace.objects.get(id = w_id)
    wspace.name = request.POST.get('workspace_name')
    wspace.description = request.POST.get('workspace_description')
    wspace.save()
    template_name = 'workspace/index.html'
    context = {
        'user': user.objects.get(id=u_id),
        'work_space': wspace,
        'boards': wspace.board_set.all(),
        'added_usrs': user.objects.filter(w_usrs__pk=w_id),
        'permissions_list': workspace_permissions.objects.filter(workspace_id=wspace),
        'not_added_usrs': user.objects.exclude(w_usrs__pk=w_id),
    }
    return render(request, template_name, context=context)


def workspace_delete(request, u_id, w_id):
    w = workspace.objects.get(id=w_id)
    w.delete()
    template_name = 'main/index.html'
    context = {
        'user': user.objects.get(id=u_id),
        'workspace': user.objects.get(id=u_id).workspace_permissions_set.all()
    }
    return redirect('/'+str(u_id))


def board_delete(request, u_id, w_id):
    wspace= workspace.objects.get(id=w_id)
    b = wspace.board_set.get(id=request.POST.get('board_to_delete'))
    b.delete()

    template_name = 'workspace/index.html'
    context = {
        'user': user.objects.get(id=u_id),
        'work_space': wspace,
        'boards': wspace.board_set.all(),
        'added_usrs': user.objects.filter(w_usrs__pk=w_id),
        'permissions_list': workspace_permissions.objects.filter(workspace_id=wspace),
        'not_added_usrs': user.objects.exclude(w_usrs__pk=w_id),
    }
    return render(request, template_name, context=context)


def user_permission_change(request, u_id, w_id):
    wspace = workspace.objects.get(id=w_id)
    user_to_change = user.objects.get(id=request.POST.get('user_to_change'))
    permissions = user_to_change.workspace_permissions_set.get(workspace_id=wspace)

    if request.POST.get('1_p') == 'on':
        permissions.permission_add_board = True
    else:
        permissions.permission_add_board = False

    if request.POST.get('2_p') == 'on':
        permissions.permission_add_file = True
    else:
        permissions.permission_add_file = False

    if request.POST.get('3_p') == 'on':
        permissions.permission_add_user = True
    else:
        permissions.permission_add_user = False

    if request.POST.get('4_p') == 'on':
        permissions.permission_change_workspace = True
    else:
        permissions.permission_change_workspace = False

    if request.POST.get('5_p') == 'on':
        permissions.permission_delete_workspace = True
    else:
        permissions.permission_delete_workspace = False

    if request.POST.get('6_p') == 'on':
        permissions.permission_delete_user = True
    else:
        permissions.permission_delete_user = False

    if request.POST.get('7_p') == 'on':
        permissions.permission_read_boards = True
    else:
        permissions.permission_read_boards = False

    permissions.save()
    template_name = 'workspace/index.html'
    context = {
        'user': user.objects.get(id=u_id),
        'work_space': wspace,
        'boards': wspace.board_set.all(),
        'added_usrs': user.objects.filter(w_usrs__pk=w_id),
        'permissions_list': workspace_permissions.objects.filter(workspace_id=wspace),
        'not_added_usrs': user.objects.exclude(w_usrs__pk=w_id),
    }
    return render(request, template_name, context=context)
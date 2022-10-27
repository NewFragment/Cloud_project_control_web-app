from django.shortcuts import render
from home.models import *


def main(request, u_id):
    usr = user.objects.get(id = u_id)

    if request.method == "POST":
        wn = request.POST.get("workspace_name")
        wd = request.POST.get("workspace_description")
        w = workspace(name = wn, description = wd)
        w.save()
        usr.w_usrs.add(w)

    template_name = 'main/index.html'
    context = {
        'user': usr,
        'workspace': usr.workspace_permissions_set.all()

    }
    return render(request, template_name, context=context)


def profile_settings(request, u_id):

    usr = user.objects.get(id=u_id)
    if request.method == "POST":
        usr = user.objects.get(id=u_id)
        usr.name = request.POST.get('name')
        usr.email = request.POST.get('email')
        usr.save()

    template_name = 'main/settings.html'
    context = {
        'user': usr,
        'workspace': usr.workspace_permissions_set.all()

    }
    return render(request, template_name, context=context)

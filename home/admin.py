from django.contrib import admin
from .models import *

admin.site.register(user)
admin.site.register(workspace)
admin.site.register(workspace_permissions)
admin.site.register(board)
admin.site.register(task)

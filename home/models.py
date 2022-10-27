from django.db import models


class user(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.name


class workspace(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    workspace_users = models.ManyToManyField(user, related_name="w_usrs", through='workspace_permissions', through_fields=('workspace_id', 'user_id'))

    def __str__(self):
        return self.name


class workspace_permissions(models.Model):
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    workspace_id = models.ForeignKey(workspace, on_delete=models.CASCADE)
    is_creator = models.BooleanField(default=True)
    permission_add_board = models.BooleanField(default=True) # 1-добавление/удаление досок
    permission_add_file = models.BooleanField(default=True) # 2-добавление /удаление файлов
    permission_add_user = models.BooleanField(default=True) # 3-добавление пользователей
    permission_change_workspace = models.BooleanField(default=True) # 4-изменение рабочего пространства
    permission_delete_workspace = models.BooleanField(default=True) # 5-удаление рабочего пространства
    permission_delete_user = models.BooleanField(default=True) # 6-удаление пользователей
    permission_read_boards = models.BooleanField(default=True) # 7-просматривать доски
    def __str__(self):
        return self.user_id.name


class board(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    workspace_id = models.ForeignKey(workspace, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class board_files(models.Model):
    board_id = models.ForeignKey(board, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='board_files/')

    def __str__(self):
        return self.file


class task(models.Model):
    board_id = models.ForeignKey(board, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    state = models.IntegerField()
    order = models.IntegerField()
    file = models.FileField(upload_to='', null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

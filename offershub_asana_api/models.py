from django.db import models
from .api import AsanaAPI

asana_instance = AsanaAPI() #instance of AsanaAPI class

'''
Below there are three classes Project, User, Task which implement creating objects
and puting it to the database. Thanks "save" function we are sending or updating data in asana
'''

class Project(models.Model):
    project_name = models.CharField(max_length=255, unique=True, name='Имя проекта')
    project_id = models.CharField(max_length=255)

    def save(self):
        if not self.id: # If the instance wasn't send we are creating it ELSE update existing instance (It is acting for all save functions) 
            project = asana_instance.create_project(self.project_name)
            self.project_id = project['gid']
            super(Project, self).save()
        else:
            asana_instance.update_project(self.project_id, self.project_name)
            super(Project, self).save()

    def __str__(self):
        return 'Project: ' + self.project_name

    class Meta:
        ordering = ["project_name"]
        verbose_name_plural = 'Проекты'


class User(models.Model):
    user_email = models.EmailField(name='Email')
    user_name = models.CharField(max_length=50, name='Имя исполнителя')
    user_id = models.CharField(max_length=255)

    def save(self):
        if not self.id:
            user = asana_instance.add_user(self.user_email)
            self.user_id = user['gid']
        super(User, self).save()

    def __str__(self):
        return 'User: ' + self.user_name

    class Meta:
        ordering = ["user_name"]
        verbose_name_plural = 'Пользователи'


class Task(models.Model):
    task_id = models.CharField(max_length=255)
    task_name = models.TextField(name='Название задания')
    executor_link = models.ForeignKey(User, on_delete=models.CASCADE, name='Имя исполнителя')
    project_link = models.ForeignKey(Project, on_delete=models.CASCADE, name='Название проекта')
    
    def save(self):
        if not self.id:
            task = asana_instance.create_task([self.project_link.project_id], self.executor_link.user_id, self.task_name)
            self.task_id = task['gid']
            super(Task, self).save()
        else:
            asana_instance.update_task(self.task_id, self.executor_link.user_id, self.task_name)
            super(Task, self).save()

    def __str__(self):
        return f'Task: {self.task_name}, implementor: {self.executor_link.user_name}, project: {self.project_link.project_name}'

    class Meta:
        ordering = ["task_name"]
        verbose_name_plural = 'Задания'


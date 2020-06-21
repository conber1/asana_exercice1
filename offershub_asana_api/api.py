import asana
from offershub_root.settings import ACCESS_TOKEN


class AsanaAPI:

    def __init__(self): #Here initialising default value of the variables (constructor)
        self.client = self.get_client() #Initialing the client
        self.workspace_id = self.get_workspace_id() #Getting workspace id 

    def get_client(self):
        return asana.Client.access_token(ACCESS_TOKEN) 

    def get_workspace_id(self): 
        return asana.Client.access_token(ACCESS_TOKEN).users.me()['workspaces'][0]['gid']

    def create_project(self, name): #Puting the new project to asana
        return self.client.projects.create_in_workspace(
            self.workspace_id, 
            {'name': name}
        )

    def update_project(self, project_id, name): #Changing existing project in asana 
        return self.client.projects.update(
            project_id,
            {'name': name}
        )

    def add_user(self, user): #Adding new user to asana
        return self.client.workspaces.add_user(
            self.workspace_id, 
            {'user': user}
        )

    def create_task(self, projects, assignee, name): #Creating new task in asaka 
        return self.client.tasks.create_in_workspace(
            self.workspace_id,
            {'projects': projects, 'assignee': assignee, 'name': name}
        )

    def update_task(self, task, assignee, name): #Updating existing task in asana 
        return self.client.tasks.update(
            task,
            {'assignee': assignee, 'name': name}
        )
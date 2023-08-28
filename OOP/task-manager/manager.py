"""Task Manager"""
class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = 'Not Started'

    def display_task_information(self):
        return f"\nTitle: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nPriority: {self.priority}\nStatus: {self.status}\n"

    def update_status(self, new_status):
        self.status = new_status
        
class TaskList:
    """represent a collection of tasks"""
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def update_task(self, task,new_status):
        task.update_status(new_status)

    def display_tasks(self):
        for task in self.tasks:
            print(task.display_task_information())

class User(TaskList):
    def __init__(self, username, email):
        super().__init__()
        self.username = username
        self.email = email



#creating instances of Task class
t1 = Task('Read Book', 'Read first chapter of a book', '2023-09-05', 'Low')
t2 = Task('Complete Project', 'Finish the project on time', '2023-09-15', 'High')

#creating instances of the User class
u1 = User('Khae', 'khae@example.com')
u2 = User('Tim', 'tim@example.com')

#adding tasks to user's task lists
u1.add_task(t1)
u2.add_task(t2)

#updating the task status
u1.update_task(t1, 'In Progress')
u2.update_task(t2,'Completed')

#display task from each user
u1.display_tasks()
u2.display_tasks()

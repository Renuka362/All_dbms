class Task:
    def __init__(self,description =None ,iscompleted = None):
        self.description = description
        self.iscompleted = iscompleted

class TaskDueDate(Task):
    def __init__(self,description,iscompleted,date=0):
        super().__init__(description,iscompleted)
        self.date = date
      
      
class TaskWithAuthor(TaskDueDate):
    def __init__(self,description,iscompleted,date,author=None):
        super().__init__(description,iscompleted,date)
        self.author = author
        
task_obj = Task('description','Yes')        
print(task_obj.description)
taskdate_obj = TaskDueDate('renuka','no',12)
print(taskdate_obj.date)
print(taskdate_obj.description)
print(task_obj.iscompleted)
taskauthor_obj = TaskWithAuthor('hi','yes',23,'Rohnald')   
print(taskauthor_obj.author)

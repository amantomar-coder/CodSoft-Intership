class ToDoList:
  def __init__(self):
      self.tasks = []

  def add_task(self, task):
      self.tasks.append(task)
      print(f'Task "{task}" added.')

  def update_task(self, index, new_task):
      if 0 <= index < len(self.tasks):
          old_task = self.tasks[index]
          self.tasks[index] = new_task
          print(f'Task "{old_task}" updated to "{new_task}".')
      else:
          print("Invalid task number.")

  def remove_task(self, index):
      if 0 <= index < len(self.tasks):
          removed_task = self.tasks.pop(index)
          print(f'Task "{removed_task}" removed.')
      else:
          print("Invalid task number.")

  def view_tasks(self):
      if self.tasks:
          for i, task in enumerate(self.tasks, 1):
              print(f'{i}. {task}')
      else:
          print("No tasks in the list.")

if __name__ == "__main__":
  todo_list = ToDoList()

  while True:
      print("\n1. Add Task\n2. Update Task\n3. Remove Task\n4. View Tasks\n5. Exit")
      choice = input("Choose an option: ")

      if choice == '1':
          task = input("Enter the task: ")
          todo_list.add_task(task)
      elif choice == '2':
          task_number = int(input("Enter the task number to update: ")) - 1
          new_task = input("Enter the new task: ")
          todo_list.update_task(task_number, new_task)
      elif choice == '3':
          task_number = int(input("Enter the task number to remove: ")) - 1
          todo_list.remove_task(task_number)
      elif choice == '4':
          todo_list.view_tasks()
      elif choice == '5':
          break
      else:
          print("Invalid option.")

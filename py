
class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Виконано" if self.completed else "Не виконано"
        return (f"Назва: {self.title}\n"
                f"Опис: {self.description}\n"
                f"Дедлайн: {self.deadline}\n"
                f"Стан: {status}\n")


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Завдання додано!")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print("Завдання видалено!")
                return
        print("Завдання не знайдено!")

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                print("Завдання виконано!")
                return
        print("Завдання не знайдено!")

    def print_tasks(self):
        if not self.tasks:
            print("Список завдань порожній.")
        else:
            for task in self.tasks:
                print(task)

manager = TaskManager()

task1 = Task("Домашня робота", "Виконати Python", "05.11.2026")
task2 = Task("Прочитати книгу", "Прочитати 10 сторінок", "06.11.2026")

manager.add_task(task1)
manager.add_task(task2)

print("\nСписок завдань:")
manager.print_tasks()

manager.mark_task_completed("Домашня робота")

manager.remove_task("Прочитати книгу")

print("\nОновлений список завдань:")
manager.print_tasks()

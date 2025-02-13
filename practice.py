class Project():
    def __init__(self, name, budget, tasks):
        self.name = name
        self.budget = budget
        self.tasks = tasks

        self.is_finished = False
        self.spent_time = 0
        self.expenses = 0

    def display_info(self):
        print(f"Проєкт {self.name}")
        print(f"Витрачено {self.spent_time} місяців")
        print(f"витрачено {self.expenses}/{self.budget}$")
        print(f"Залишилось {self.budget - self.expenses}$")

        if self.is_finished:
            print("Стан проєкту: завершанний")
        else:
            print("Стан проєкту: незавершанний")
            print("Задачі що залишились:")
            for task in self.tasks:
                print(f"    - {task}")


project = Project (name="Ігрушка",
                   budget=10_000,
                   tasks=['Знайти інвесторів',
                          'Придумати загальну ідею' ])

project.display_info()
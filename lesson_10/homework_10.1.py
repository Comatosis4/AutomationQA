class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

dev = Developer('Bob', 20000, 'Python')
manager = Manager('Tom', 21000, 'QA')
lead = TeamLead(dev.name, manager.salary, manager.department, dev.programming_language, 3)
print(lead.team_size)
print(lead.department)
print(lead.name)

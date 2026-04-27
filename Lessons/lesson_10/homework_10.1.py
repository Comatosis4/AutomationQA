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

    def test_atr(self):
        assert hasattr(self, "programming_language"), "Missing attribute: programming_language"
        print(self.programming_language)
        assert hasattr(self, "department"), "Missing attribute: department"
        print(self.department)
        assert hasattr(self, "name"), "Missing attribute: name"
        print(self.name)
        assert hasattr(self, "salary"), "Missing attribute: salary"
        print(self.salary)
        assert hasattr(self, "team_size"), "Missing attribute: team_size"
        print(self.team_size)


dev = Developer('Bob', 20000, 'Python')
manager = Manager('Tom', 21000, 'QA')
lead = TeamLead(dev.name, manager.salary, manager.department, dev.programming_language, 3)
lead.test_atr()

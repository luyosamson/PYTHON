class Employee:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department
    def info(self):
        print(f'Name:{self.name}, of ID {self.id} from department of {self.department}')
class Developer(Employee):
    def __init__(self,name,id,department,programming_language,year_of_experience):
        super.__init__(name,id,department)
        self.programming_language=programming_language
        self.year_of_experience=year_of_experience
    def details(self):
        print(f'Name:{self.name},year of experience:{self.year_of_experience},programming language {self.programming_language}')
class Manager(Employee):
    def __init__(self,name,id,department,team_size,manager_level):
        Employee.__init__(self,name,id,department)
        self.team_size=team_size
        self.manager_level=manager_level
    def info(self):
        print(f'Name:{self.name},team size {self.team_size},manager level {self.manager_level}')
manager=Manager("Luyo","M7","ICT",34,"Senior")
manager.info()
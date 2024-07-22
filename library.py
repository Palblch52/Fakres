class Employee:
    def __init__(self, fam='', name='', surname='', division='', days='', salary=''):
        self.fam = fam
        self.name = name
        self.surname = surname
        self.division = division
        self.days = days
        self.salary = salary
    
    def getEmployee_forTable(self):
        w = []
        w.append(self.fam)
        w.append(self.name)
        w.append(self.surname)
        w.append(self.division)
        w.append(self.days)
        w.append(self.salary)
        return w
    
    def equval_Employee(self,B):
    
        return self.fam == B.fam and \
               self.name == B.name and \
               self.surname == B.surname and \
               self.division == B.division and \
               self.days == B.days and \
               self.salary == B.salary

class Grup:
    def __init__(self):
        self.A = {}
        self.count = 0
    
    def __str__(self):
        s = ''
        for x in range(len(self.A)): 
            if x in self.A:
                s += f'Employee {x+1}:\n'
                s += str(self.A[x])
                s += '\n'
        return s   

    def appendEmployee(self, List):
        new_Employee = Employee(*List)
        self.A[self.count] = new_Employee

        self.count += 1
    
    def editEmployee(self,x,List):
        P = Employee(*List)
        self.A[x] = P

    def Str_Employee(self,line):
        if line[-1] == '\n' : line = line[:-1] 
        parts = line.strip().split("&")

        return Employee(*parts)
    
    def read_data(self, file_name):
        self.A = {}
        x = 0
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                self.A[x] = self.Str_Employee(line)

                x += 1
                self.count += 1

    def find_keyEmployee(self, List):

        P = Employee(*List)
        for x in self.A :
            
            if self.A[x].equval_Employee(P) :
               return x

        return -1    

    def delEmployee(self, List):
        P = Employee(*List)
        for x in self.A :
            if self.A[x].equval_Employee(P):
                del self.A[x] 
                self.count = self.count- 1
    
                break          
            
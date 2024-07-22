class Employee:
    def __init__(self, fam, name, surname, division, days, salary):
        self.fam = fam
        self.name = name
        self.surname = surname
        self.division = division
        self.days = days
        self.salary = salary
    
    def getEmployee_forTable(self):
        w = []
        print(self.fam+' '+self.name+' '+self.surname)
        x = self.fam+' '+self.name+' '+self.surname
        w.append(x)
        w.append(self.division)
        w.append(self.days)
        w.append(self.salary)
        print(w)
        return w

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

    def appendEmployee(self, str_Employee):
        parts = str_Employee.strip().split(" ")
        self.A[self.count] = Employee(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])

        self.count += 1
        with open('text.txt', 'a', encoding='utf-8') as file:
            file.write('\n' + str_Employee)

    def read_data(self, file_name):
        self.A = {}
        x = 0
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                if line[-1] == '\n': line = line[:-1]
                parts = line.strip().split(" ")
                
                self.A[x] = Employee(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])

                x += 1
                self.count += 1
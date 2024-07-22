class Employee:
    def __init__(self, fam='', name='', surname='', division='', days='', salary=''):
        """
        Инициализация объекта Employee с заданными атрибутами.
        fam: фамилия сотрудника
        name: имя сотрудника
        surname: отчество сотрудника
        division: подразделение сотрудника
        days: количество отработанных дней
        salary: зарплата сотрудника
        """
        self.fam = fam
        self.name = name
        self.surname = surname
        self.division = division
        self.days = days
        self.salary = salary
    
    def get_employee_for_table(self):
        """
        Возвращает данные сотрудника в виде списка.
        Используется для отображения данных в таблице.
        """
        return [self.fam, self.name, self.surname, self.division, self.days, self.salary]
    
    def equval_employee(self, other):
        """
        Сравнивает два объекта Employee на равенство по их атрибутам.
        other: объект Employee для сравнения
        Возвращает True, если все атрибуты равны, иначе False.
        """
        return (self.fam == other.fam and self.name == other.name and
                self.surname == other.surname and self.division == other.division and
                self.days == other.days and self.salary == other.salary)

class Grup:
    def __init__(self):
        """
        Инициализация объекта Grup с пустым словарем сотрудников и счетчиком.
        self.A: словарь сотрудников
        self.count: количество сотрудников
        """
        self.A = {}
        self.count = 0
    
    def __str__(self):
        """
        Возвращает строковое представление объекта Grup.
        Включает данные всех сотрудников в группе.
        """
        s = ''
        for x in range(len(self.A)): 
            if x in self.A:
                s += f'Сотрудник {x+1}:\n'
                s += str(self.A[x].get_employee_for_table())
                s += '\n'
        return s   

    def append_employee(self, employee_list):
        """
        Добавление нового сотрудника в группу.
        employee_list: список атрибутов сотрудника
        """
        new_employee = Employee(*employee_list)
        self.A[self.count] = new_employee
        self.count += 1
    
    def edit_employee(self, index, employee_list):
        """
        Редактирование существующего сотрудника в группе.
        index: индекс сотрудника в словаре
        employee_list: новый список атрибутов сотрудника
        """
        updated_employee = Employee(*employee_list)
        self.A[index] = updated_employee

    def str_employee(self, line):
        """
        Преобразование строки текста в объект Employee.
        line: строка с данными сотрудника, разделенными "&"
        Возвращает объект Employee.
        """
        if line.endswith('\n'):
            line = line[:-1] 
        parts = line.strip().split("&")
        return Employee(*parts)
    
    def read_data(self, file_name):
        """
        Чтение данных сотрудников из файла и заполнение группы.
        file_name: имя файла с данными
        """
        self.A = {}
        self.count = 0
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                self.A[self.count] = self.str_employee(line)
                self.count += 1

    def find_key_employee(self, employee_list):
        """
        Поиск ключа сотрудника в группе по его атрибутам.
        employee_list: список атрибутов сотрудника
        Возвращает ключ сотрудника, если найден, иначе -1.
        """
        employee = Employee(*employee_list)
        for key, emp in self.A.items():
            if emp.equval_employee(employee):
                return key
        return -1    

    def del_employee(self, employee_list):
        """
        Удаление сотрудника из группы.
        employee_list: список атрибутов сотрудника для удаления
        """
        employee = Employee(*employee_list)
        for key, emp in self.A.items():
            if emp.equval_employee(employee):
                del self.A[key] 
                self.count -= 1
                break
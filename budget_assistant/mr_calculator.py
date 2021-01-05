# INCOME, SAVING, FIXED EXPENSE, TRAVEL, HEALTH
# FOR TEST INHERITANCE

import hashlib

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class SalaryMan(Person):
    def __init__(self, first_name, last_name, salary, classified=False):
        super().__init__(first_name, last_name)
        self.salary = salary
        self.classified = classified
        self.last_name =  self.verify_data(self.last_name)
        self.salary =  self.verify_data(str(self.salary))
    
    def verify_data(self, data):
        return self.classify_data(data) if self.classified else data

    def classify_data(self, data):
        md5_obj = hashlib.md5()
        md5_obj.update(str.encode(data))
        return  md5_obj.digest()


    def print_info(self):
        print("-" * 100)
        print(f"Secured Mode: {self.classified}")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Salary: {self.salary}")
        

if __name__ == "__main__":
    chopper = SalaryMan('Chopper', 'Tonytony', 99000000, classified=True)
    chopper.print_info()

    zoro = SalaryMan('Zoro', 'Roronoa', 500000000, classified=False)
    zoro.print_info()

    print("-" * 100)
    
class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        print(f"Original bill: P{self.__bill_amount}")
        print(f"Final bill: P{self.__bill_amount}")


class SeniorPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
    
    def calculate_bill(self):
        self.finalBill = self.__bill_amount * 0.8
        print(f"Original bill: P{self.bill_amount}")
        print(f"Final bill : P{self.finalBill}")
 
 
class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
    
    def calculate_bill(self):
        discount = self.get_bill_amount() * .15
        return self.get_bill_amount() - discount
    
patient = Patient("Juan Dela Cruz", 15000)
print("Patient name:", patient.get_name())
patient.calculate_bill()

seniorpatient = SeniorPatient("Maria Santos", 15000)
print("Patient name:", senior.get_name())
senior.calculate_bill()


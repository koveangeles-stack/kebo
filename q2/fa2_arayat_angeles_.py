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

    def calculate_bill():
      print("Patient Name:", self.__name)
      print("\nOriginal Bill:", self.__bill_amount)
      print("\nFinal Bill:", self.__bill_amount)

regular_patient = Patient("Juan Dela Cruz", 15000)

print(f"Patient Name: {regular_patient.get_name()}")


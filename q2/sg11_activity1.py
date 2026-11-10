class Patient: #Creates a parent class, patient
    def __init__(self, name, bill_amount): #The attribute of the parent class
        self.__name = name #The name of the Patient
        self.__bill_amount = bill_amount #The initial bill amount of the Patient without any discounts
    def get_name(self): #A method that gets the name of the patient
        print(f'Patient Name: {self.__name}') #Gets and prints the name of the patient - Sample Output: Juan De La Cruz
    def set_name(self, name): #A method that sets the name of the patient
        self.__name = name #Sets the name of the patient based on the inputted value by the user
    def get_bill_amount(self): #A method that gets the initial bill amount of the patient
        print(f'Original Bill: ₱{self.__bill_amount:.2f}') #Gets and prints the bill amount of the patient - Sample Output: Original Bill: ₱15000
    def set_bill_amount(self, bill_amount): #A method that sets the bill amount of the patient
        self.__bill_amount = bill_amount #Sets the bill amount of the patient
    def calculate_bill(self): #Calculates the bill amount of the patient after discount
        print(f'Final Bill: ₱{self.__bill_amount:.2f}') #Prints the final bill of the patient with the discount - Sample Output: Final Bill: ₱15000
    def display_patient_type(self): #Displays the patient type
        print("Regular Patient") #Prints the patient type - Output: Regular Patient

class Senior(Patient): #A child class that inherits the attributes and methods of the parent class, Patient
    def calculate_bill(self): #Overrides the inherited method to reflect its final bill with its respective discount
        print(f'Final Bill: ₱{(self._Patient__bill_amount*0.80):.2f}') #Prints and calculates the final bill with the 20% discount - Sample Output: Final Bill: ₱12000
    def display_patient_type(self): #Overrides the inherited method and displays the patient type
        print("Senior Citizen") #Prints the patient type - Output: Senior Citizen

class PhilHealth(Patient): #A child class that inherits the attributes and methods of the parent class, Patient
    def calculate_bill(self): #Overrides the inherited method to reflect its final bill with its respective discount
        print(f'Final Bill: ₱{(self._Patient__bill_amount*0.85):.2f}') #Prints and calculates the final bill with the 15% discount - Sample Output: Final Bill: ₱12750
    def display_patient_type(self): #Overrides the inherited method and displays the patient type
        print("Patient Type: PhilHealth Member") #Prints the patient type - Output: PhilHealth Member

patient1 = Patient("Juan Dela Cruz", 15000)
senior1 = Senior("Maria Santos", 15000)
philhealth1 = PhilHealth("Pedro Reyes", 15000)

print("Hospital Billing System")
print("-----------------------")
patient1.get_name()
patient1.display_patient_type()
patient1.get_bill_amount()
patient1.calculate_bill()
print()
senior1.get_name()
senior1.display_patient_type()
senior1.get_bill_amount()
senior1.calculate_bill()
print()
philhealth1.get_name()
philhealth1.display_patient_type()
philhealth1.get_bill_amount()
philhealth1.calculate_bill()

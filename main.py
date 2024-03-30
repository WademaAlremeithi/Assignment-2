#define an empty list to store patients records
patients =[]
#define Patient class to represent patient infromation
class Patient :
    def __init__(self, name, dob, gender, phone_number, allergies, past_illness, vaccines, current_conditions, medications, assigned_doctor, appointment_date, appointment_time):
        #initialize patient attributes 
        self.name = name
        self.dob = dob
        self.gender = gender
        self.phone_number = phone_number
        self.allergies = allergies
        self.past_illness = past_illness
        self.vaccines = vaccines
        self.current_conditions = current_conditions
        self.medications = medications
        self.assigned_doctor = assigned_doctor 
        self.appointment_date = appointment_date 
        self.appointment_time = appointment_time

    #getter methods
    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def get_gender(self):
        return self.gender
        
    def get_phone_number(self):
        return self.phone_number

    def get_allergies(self):
        return self.allergies

    def get_past_illness(self):
        return self.past_illness

    def get_vaccines(self):
        return self.vaccines

    def get_current_conditions(self):
        return self.current_conditions

    def get_assigned_doctor(self):
        return self.assiend_doctor
    
    def get_appointment_date(self):
        return self.appointment_date 

    def get_appointment_time(self):
        return self.appointment_time

    #setter methods
    def set_name(self, name):
        self.name = name

    def set_dob(self, dob):
        self.dob = dob

    def set_gender(self, gender):
        self.gender = gender

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_allergies(self, allergies):
        self.allergies = allergies

    def set_past_illness(self, past_illness):
        self.past_illness = past_illness

    def set_vaccines(self, vaccines):
        self.vaccines = vaccines

    def set_current_conditions(self, current_conditions):
        self.current_conditions = current_conditions

    def set_assigned_doctor(self, assigned_doctor):
        self.assigned_doctor = assigned_doctor 
    def set_appointment_date(self, appointment_date):
        self.appointment_date = appointment_date
        
    def set_appointment_time(self, appointment_time):
        self.appointment_time = appointment_time
        
    #method to store patient record
    def  store_patient(self):
        patients.append(self.name)
        return patients

    #override __str__ to display patient Information 
    def __str__(self):
        return f"Name: {self.name}, Date of Birth: {self.dob}, Gender: {self.gender}, Phone Number: {self.phone_number}, Allergies: {self.allergies}, Past Illness: {self.past_illness}, Vaccines: {self.vaccines}, Current Condition: {self.current_conditions}, Medications: {self.medications}, Assigned Doctor: {self.assigned_doctor}, Appointment Date: {self.appointment_date}, Appointment Time: {self.appointment_time}"

#define the Doctor class to represent doctor information
class Doctor :
    def __init__(self, name, id, department, assigned_patients):
        self.name = name
        self.id = id
        self.department = department
        self.assigned_patients = assigned_patients

    #getter methods
    def get_name(self):
        return self.name
            
    def get_id(self):
        return self.id
            
    def get_department(self):
        return self.department
            
    def get_assigned_patients(self):
        return self.assigned_patients
            
    #setter methods
    def set_name(self, name):
        self.name = name

    def set_id(self, id):
        self.id = id

    def set_department(self, department):
        self.department = department
        
    def set_assigned_patients(self, patients):
        self.assigned_patients.append(patients)

#define the Queue class for managing the consultation queue of patients
class Queue: 
    def __init__(self):
        self.items = []

    #check if the queue is empty 
    def isEmpty(self):
        return self.items == []

    #add an item to the queue
    def enqueue(self, item):
        self.items.insert(0, item)

    #remove an item from the queue
    def dequeue(self):
        return self.items.pop()

    #get the size of the queue
    def size(self):
        return len(self.items)

    #override __str__ method to display queue items
    def __str__(self):
        return str(self.items)
        
#define the Stack class for managing prescriptions
class Stack:
    def __init__(self):
        self.stack = []

    #push an item onto the stack
    def push(self, item):
        self.stack.append(item)

    #pop an item from the stack
    def pop(self):
        return self.stack.pop()

    #peek at the top item of the stack
    def peek(self):
        return self.stack[len(self.stack) - 1]

    #override __str__ method to display stack items
    def __str__(self):
        return str(self.stack)

    #check if the stack is empty 
    def isEmpty(self):
        return self.stack == []

    #get the size of the stack
    def size(self):
        return len(self.stack)        

#create a consultation queue for the patients 
consultation_queue = Queue()
for i in patients:
    consultation_queue.enqueue(i)

#create a stack for prescriptions
prescriptions = Stack()
for patient in patients:
    for i in patient.medications:
       prescriptions.push(i)
    print(patient.name, "'s prescripstions are", prescriptions)
#create a dictionary for storing appointments 
appointments = {}

#function to schedule an appointment for a patient with a doctor 
def schedule_appointment(patient, doctor, appointment_time, appointment_date):
    if doctor not in appointments:
        appointments[doctor] = {}
    if appointment_date not in appointments[doctor]:
        appointments[doctor][appointment_date] ={}
    if appointment_time not in appointments[doctor][appointment_date]:
        appointments[doctor][appointment_date][appointment_time] = patient
        print("Appointment sceduled for", patient, "with", doctor, "at", appointment_time, "on", appointment_date)
        patient.set_assigned_doctor(doctor)
        patient.set_appointment_date(appointment_date)
        patient.set_appointment_time(appointment_time)

#function to cancel an appointment 
def cancel_appointment(doctor, appointment_time, appointment_date):
    patient = appointments[doctor][appointment_date].pop(appoinment_time)
    print("Appointment Cancelled !")
    patient.set_assigned_doctor("")
    patient.set_appointment_date("")
    patient.set_appointment_time("")

#function to search for a patient record 
def search_patient(patient):
    if patient.name in patients:
        print("Patient Records Found !")
        print(patient)
    else:
        print("Patient NOT found!")

#function to add a new patient 
def add_patient():
    name = input("Enter patient's name: ")
    dob = input("Enter patient's date of birth: ")
    gender = input("Enter patient's gender: ")
    phone_number = input("Enter patient's phone number: ")
    allergies = input("Enter patient's allergies, if any: ")
    past_illness = input("Enter patient's past illness, if any: ")
    vaccines = input("Enter patient's vaccines: ")
    current_conditions = input("Enter patient's current condition: ")
    medications = input("Enter patient's medications, if any: ")
    assigned_doctor = input("Enter assigned doctor: ")
    appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
    appointment_time  = input("Enter appointment time: ")
    
    patient = Patient(name, dob, gender, phone_number, allergies, past_illness, vaccines, current_conditions, medications, assingned_doctor, appointment_date, appointment_time)
    patient.store_patient()
    print("Patient record added successfully")

#function to update a patient record
def update_patient():
    name = input("Enter patient's name to update: ")
    for patient in patients:
        if patient.name == name:
            assigned_doctor = input("Enter updated assigned doctor: ")
            appointment_date = input("Enter updated appointment date (YYYY-MM-DD): ")
            appointment_time = input("Enter updated appointment time: ")
            patient.set_assigned_doctor(assigned_doctor)
            patient.set_appointment_date(appointment_date)
            patient.set_appointment_time(appointment_time)
            print("Patient record updated successfully")
            return
    print("Patient not found")
            







patients =[]
#Patient class
class Patient :
    def __init__(self, name, dob, gender, phone_number, allergies, past_illness, vaccines, current_conditions, medications, assiend_doctor, appointment_date, appointment_time):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.phone_number = phone_number
        self.allergies = allergies
        self.past_illness = past_illness
        self.vaccines = vaccines
        self.current_conditions = current_conditions
        self.medications = medications
        self.assiend_doctor = assiend_doctor 
        self.appointment_date = appointment_date 
        self.appointment_time = appointment_time

        #getters
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

        def get_assiend_doctor(self):
            return self.assiend_doctor

        def get_appointment_date(self):
            return self.appointment_date 

        def get_appointment_time(self):
            return self.appointment_time

        #setters
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

        def set_assiend_doctor(self, assiend_doctor):
            self.assiend_doctor = assiend_doctor 
        
        def  store_patient(self, name):
            patients.append(name)
            return patients

class Doctor :
    def __init__(self, name, id, department, assigned_patients):
        self.name = name
        self.id = id
        self.department = department
        self.assigned_patients = assigned_patients

        #getters
        def get_name(self):
            return self.name
            
        def get_id(self):
            return self.id
            
        def get_department(self):
            return self.department
            
        def get_assigned_patients(self):
            return self.assigned_patients
            
        #setters
        def set_name(self, name):
            self.name = name

        def set_id(self, id):
            self.id = id

        def set_department(self, department):
            self.department = department
        
        def set_assigned_patients(self, patients):
            self.assigned_patients.append(patients)

class Queue: #this creates the class for the queue data structure to be used for the consultation queue of patients
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
        
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def __str__(self):
        return str(self.stack)

    def isEmpty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)        
consultation_queue = Queue()
for i in patients:
    consultation_queue.enqueue(i)
prescriptions = Stack()
for patient in patients:
    for i in patient.medications:
       prescriptions.push(i)
    print(patient.name, "'s prescripstions are", prescriptions)












patients =[]
#Patient class
class Patient :
    def __init__(self, name, dob, gender, phone_number, allergies, past_illness, vaccines, current_conditions):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.phone_number = phone_number
        self.allergies = allergies
        self.past_illness = past_illness
        self.vaccines = vaccines
        self.current_conditions = current_conditions

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
        
        def  store_patient(self, name):
            patients.append(name)
            return patients

class Doctors :
    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department

        #getters
        def get_name(self):
            return self.name
            
        def get_id(self):
            return self.id
            
        def get_department(self):
            return self.department
            
        #setters
        def set_name(self, name):
            self.name = name

        def set_id(self, id):
            self.id = id

        def set_department(self, department):
            self.department = department

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














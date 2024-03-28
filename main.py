# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

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
        















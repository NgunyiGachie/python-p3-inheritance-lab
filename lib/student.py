#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name, knowledge=None):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge if knowledge is not None else []

    def learn(self, new_information):
        if isinstance(new_information, str):
            self.knowledge.append(new_information)
        elif isinstance(new_information, list):
            self.knowledge.extend(new_information)
        else:
            raise TypeError("new_information must be a string or a list of strings")

        
    
#!/usr/bin/python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (pickle.PickleError, IOError) as e:
            print(f"Serialization error: {e}")

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                else:
                    return None
        except (FileNotFoundError, pickle.PickleError, EOFError):
            return None

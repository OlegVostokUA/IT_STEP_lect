import pickle

# pickle.dump(obj, file)

# lst = [2, 2.890, [3.4, 78]]
#
# tpl = ('wewq', 'sdsad')
#
# sett = {1:2, 2:45.987, 3:True, 4:'ertop'}
#
# file = open('myfile.bin', 'wb')
# pickle.dump(lst, file)
# file.close()
#
# file = open('myfile.bin', 'rb')
# lst2 = pickle.load(file)
# file.close()
#
# print(lst2)
# print(lst2[2][0], type(lst2[2][0]))

# numbers = [1, 2, 3, 4, 5]
#
# serial_data = pickle.dumps(numbers)
#
# print('Serialized:', serial_data)
#
# deser_data = pickle.loads(serial_data)
#
# print('Deserialized:', deser_data)
#

#########
# import os
#
# def create_path(filename):
#     scr_dir = os.path.dirname(os.path.realpath(__file__))
#     return os.path.join(scr_dir, filename)
#
#
# def serialize(filename, data):
#     with open(create_path(filename), 'wb') as file:
#         pickle.dump(data, file)
#
# def deserialize(filename):
#     with open(create_path(filename), 'rb') as file:
#         data = pickle.load(file)
#     return data
#
#
# class Person:
#     def __init__(self, f_name, l_name):
#         self.f_name = f_name
#         self.l_name = l_name
#
#     def get_full_name(self):
#         return f'{self.f_name} {self.l_name}'
#
#
# p1 = Person('Bob', 'Green')
#
# print(f'Original: {p1.get_full_name()}')
#
# file_name = 'person.bin'
#
# serialize(file_name, p1)
#
# person_r = deserialize(file_name)
#
# print(f'Restored: {person_r.get_full_name()}')
#
# print(p1 is person_r)
####
# "employee": [
#         {
#             "first_name": "Katie",
#             "last_name": "Red",
#             "age": 30,
#             "married": false,
#             "children": ["Anna", "Bill"],
#             "address": {
#                 "street": "Mersa",
#                 "city": "London"
#             }
#         },
#         {
#             "first_name": "Katie",
#             "last_name": "Red",
#             "age": 30,
#             "married": false,
#             "children": ["Anna", "Bill"],
#             "address": {
#                 "street": "Mersa",
#                 "city": "London"
#             }
#         }
#     ]

import json

# capitals = {"Italy": "Rome", "Spain": "Madrid", "Germany": "Berlin"}
#
# ser_capitals = json.dumps(capitals)
# print(f'Serialized: {ser_capitals}', type(ser_capitals))
#
# deser_capitals = json.loads(ser_capitals)
# print(f'Deserialized: {deser_capitals}', type(deser_capitals))

import os

def create_path(filename):
    scr_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(scr_dir, filename)


def serialize(filename, data):
    with open(create_path(filename), 'w') as file:
        json.dump(data, file)


def deserialize(filename):
    with open(create_path(filename), 'r') as file:
        data = json.load(file)
    return data

# file_name = 'employee.dat'
#
# emp_dict = {
#     "company": "ABC",
#     "employee": [
#                     {
#                         "first_name": "Katie",
#                         "last_name": "Red",
#                         "age": 30,
#                         "married": False,
#                         "children": ["Anna", "Bill"],
#                         "address": {
#                             "street": "Mersa",
#                             "city": "London"
#                         }
#                     },
#                     {
#                         "first_name": "Katie",
#                         "last_name": "Blue",
#                         "age": 34,
#                         "married": False,
#                         "children": ["Anna", "Bill"],
#                         "address": {
#                             "street": "Mersa",
#                             "city": "London"
#                         }
#                     }
#         ]
# }
#
# # serialize(file_name, emp_dict)
#
# des_data = deserialize(file_name)
#
# print(des_data['employee'], type(des_data))

class FootballClub:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def get(self):
        return f'{self.name} {self.city}'

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def create(json_data):
        dict_ = json.loads(json_data)
        return FootballClub(dict_['name'], dict_['city'])

fk1 = FootballClub('Dynamo', 'Kiyv')
fk2 = FootballClub('Shahtar', 'Donetsk')

#
# list_fk = [fk1, fk2]
# list_ser = []
#
# for i in list_fk:
#     list_ser.append(i.to_json())
#
# print(list_ser)
#
ser_fk = fk1.to_json()
print(ser_fk, type(ser_fk))

fk1_deser = FootballClub.create(ser_fk)

print(fk1_deser.get())
print(id(fk1_deser))



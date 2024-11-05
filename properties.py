# class Person:
#     def __init__(self, name, dob=None):
#         self.name = name
#         self.dob = dob
#
#
# p = Person("Zaklin")
# p.name = "Jane"
# p.email = "...."
# print(p.name)


# class Person:
#     def __init__(self, name):
#         self.set_name(name)
#
#     def get_name(self):
#         return self._name.capitalize()
#
#     def set_name(self, value):
#         if len(value) <= 1:
#             raise ValueError("Name is too short")
#         self._name = value
#
#
# p = Person("zaklin")
# print(p.get_name())


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self._name.capitalize()
#
#     def set_name(self, value):
#         if len(value) <= 1:
#             raise ValueError("Name is too short")
#         self._name = value
#
#     name = property(get_name, set_name)
#
#
# p = Person("zaklin")
# p.name = "Z"
# print(p.name)


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name.capitalize()

    @name.setter
    def name(self, value):
        if len(value) <= 1:
            raise ValueError("Name too short")
        self._name = value


class PersonWithInitials(Person):
    def initials(self):
        return self.name[0]


p = PersonWithInitials("zaklin")
print(p.name)
print(p.initials())

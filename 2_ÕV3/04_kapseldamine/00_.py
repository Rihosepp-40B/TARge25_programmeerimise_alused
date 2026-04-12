class Privacy:
    def __init__(self):
        self._warning = 1
        self.public = 2
        self.__private = 3

    def get_private(self):
        return self.__private

    def get_warning(self):
        return self._warning

    def get_public(self):
        return self.public

    def set_private(self, private):
        self.__private = private


a = Privacy()
print(a.get_warning())  # prindib vaikeväärtuse 1
print(a.get_public())  # prindib vaikeväärtuse 2
print(a.get_private())  # prindib vaikeväärtuse 3
a._warning = 10
a.public = 20
a.__private = 30
print(a.get_warning())  # prindib uue väärtuse 10
print(a.get_public())  # prindib uue väärtuse 20
print(a.get_private())  # prindib vaikeväärtuse 3
a.set_private(30)
print(a.get_private())
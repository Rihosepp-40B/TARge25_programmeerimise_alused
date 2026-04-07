"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""

    STATUS_ACTIVE = "Active"
    STATUS_EXPELLED = "Expelled"
    STATUS_FINISHED = "Finished"
    STATUS_INACTIVE = "Inactive"

    def __init__(self, name: str, id: int):
        """Konstruktor."""
        self.__id = id
        self.__name = name
        self.__status = Student.STATUS_ACTIVE

    def get_id(self) -> int:
        """Tagastab algselt tudengile määratud id."""
        return self.__id

    def set_name(self, name: str) -> None:
        """Määrab tudengile uue nime."""
        self.__name = name

    def get_name(self):
        """Tagastab tudengi hetke nime."""
        return self.__name

    def set_status(self, status: str) -> None:
        """Määrab tudengile uue staatuse."""
        status_list = [Student.STATUS_ACTIVE, Student.STATUS_EXPELLED, Student.STATUS_FINISHED, Student.STATUS_INACTIVE]
        if status in status_list:
            self.__status = status

    def get_status(self):
        """Tagastab tudengi hetke staatuse."""
        return self.__status


if __name__ == '__main__':
    student1 = Student("Tiit", 1)
    print(student1.get_status())
    student1.set_status("Lahkunud")
    print(student1.get_status())
    student1.set_status("finished")
    print(student1.get_status())
    student1.set_status(Student.STATUS_EXPELLED)
    print(student1.get_status())

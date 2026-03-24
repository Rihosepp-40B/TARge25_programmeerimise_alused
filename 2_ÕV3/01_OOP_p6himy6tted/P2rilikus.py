class Student:

    def say_hello(self):
        print("Hello!")


# Extending the base class
class ITStudent(Student):

    def assist_friend(self):
        print("Have you tried turning it off and on again?")


alice = Student()
mary = ITStudent()

alice.say_hello()  # --> Hello!
mary.say_hello()  # --> Hello!
alice.assist_friend()  # --> AttributeError: 'Student' object has no attribute 'assist_friend'
mary.assist_friend()  # --> Have you tried turning it off and on again?
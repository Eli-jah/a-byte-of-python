# super-class or base-class
class SchoolMember:
    """Represents any school member."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('A new school member is created:', self.name)

    def intro(self):
        print('I am {:s}, {:d} years old.'.format(self.name, self.age), end=' ')


# sub-class
class Teacher(SchoolMember):
    """Represents a teacher."""

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('A new teacher is created:', self.name)

    def intro(self):
        SchoolMember.intro(self)
        print('And my salary:', self.salary)


# sub-class
class Student(SchoolMember):
    """Represents a student."""

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('A new student is created:', self.name)

    def intro(self):
        SchoolMember.intro(self)
        print('And my marks: {:d}.'.format(self.marks))


teacher = Teacher('Wang', 30, 5000)

#  To print a blank line.
print()

student = Student('Elijah', 13, 3000)

#  To print a blank line.
print()

members = [teacher, student]
for member in members:
    member.intro()

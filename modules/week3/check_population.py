class Person:
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    def describe(self):
        pass  # This will be overridden in child classes


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}")


class Ward:
    def __init__(self, name):
        self.__name = name
        self.__list_people = []
        self.__current_year = 2024  # Fixed current year

    def add_person(self, person):
        self.__list_people.append(person)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for person in self.__list_people:
            person.describe()

    def count_doctor(self):
        return sum(1 for person in self.__list_people if isinstance(person, Doctor))

    def sort_age(self):
        self.__list_people.sort(
            key=lambda x: self.__current_year - x.get_yob())

    def compute_average(self):
        teachers = [
            person for person in self.__list_people if isinstance(person, Teacher)]
        if not teachers:
            return 0
        return sum(teacher.get_yob() for teacher in teachers) / len(teachers)


# Test
ward1 = Ward("Ward1")
ward1.add_person(Student("studentA", 2010, "7"))
ward1.add_person(Teacher("teacherA", 1969, "Math"))
ward1.add_person(Teacher("teacherB", 1995, "History"))
ward1.add_person(Doctor("doctorA", 1945, "Endocrinologists"))
ward1.add_person(Doctor("doctorB", 1975, "Cardiologists"))

ward1.describe()
print(f"\nNumber of doctors: {ward1.count_doctor()}")

print("\nAfter sorting Age of Ward1 people")
ward1.sort_age()
ward1.describe()

print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")

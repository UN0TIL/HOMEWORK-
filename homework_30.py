class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"gender = {self.gender}, age = {self.age}, first_name = {self.first_name}, last_name = {self.last_name}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"gender = {self.gender}, age = {self.age}, first_name = {self.first_name}, last_name = {self.last_name}, record_book = {self.record_book}"


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise ValueError(
                "Кол-во студентов, не должно превышать 10 человек на одну группу"
            )
        else:
            self.group.add(student)

    def delete_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                self.group.remove(student)
                break

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f"Number: {self.number}\n{all_students}"


st1 = Student("Male", 30, "Steve", "Jobs", "AN142")
st2 = Student("Female", 25, "Liza", "Taylor", "AN145")
st3 = Student("Male", 28, "John", "Doe", "AN146")
st4 = Student("Female", 22, "Emily", "Smith", "AN148")
st5 = Student("Male", 29, "Michael", "Johnson", "AN150")
st6 = Student("Female", 24, "Emma", "Williams", "AN152")
st7 = Student("Male", 27, "Daniel", "Brown", "AN154")
st8 = Student("Female", 23, "Olivia", "Jones", "AN156")
st9 = Student("Male", 26, "William", "Miller", "AN158")
st10 = Student("Female", 21, "Sophia", "Davis", "AN160")
st11 = Student("Male", 31, "James", "Wilson", "AN162")
st12 = Student("Female", 20, "Ava", "Martinez", "AN164")
gr = Group("PD1")
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
try:
    gr.add_student(st11)
    gr.add_student(st12)
except ValueError as e:
    print(e)  # Достигло максимума

print(gr)
assert str(gr.find_student("Jobs")) == str(st1), "Test1"
assert gr.find_student("Jobs2") is None, "Test2"
assert (
    isinstance(gr.find_student("Jobs"), Student) is True
), "Метод поиска должен возвращать экземпляр"

gr.delete_student("Taylor")
print(gr)  # Only one student

gr.delete_student("Taylor")  # No error!
print("OK")

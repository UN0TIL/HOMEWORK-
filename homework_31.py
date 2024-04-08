from main import Human, Student, Group


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
print('test 1')
assert gr.find_student("Jobs2") is None, "Test2"
print('test 2')
assert (
    isinstance(gr.find_student("Jobs"), Student) is True
), "Метод поиска должен возвращать экземпляр"
print('test 3')

gr.delete_student("Taylor")
print(gr)  # Only one student

gr.delete_student("Taylor")  # No error!


assert gr.find_student('Jobs') == st1
print('test 4')

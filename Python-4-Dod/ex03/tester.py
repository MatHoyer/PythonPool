from new_student import Student


student = Student(name="Edward", surname="agle")
print(student)

try:
    otherStudent = Student(name="Edward", surname="agle", id="123456789012345")
    print(otherStudent)
except Exception as e:
    print(e)

try:
    otherStudent = Student(name="Edward", surname="agle", login="edwardagle")
    print(otherStudent)
except Exception as e:
    print(e)

name = "Gustavo"
hobby = "Gaming"
age = 24
is_married = False

print("========== Variable ==========")
print("nama: %s" % (name))
print("hobi: %s, umur: %d, sudah menikah? %r" % (hobby, age, is_married))

student: str = "Alucard Sujatmiko"
major: str = "Industrial Engineering"
student_number: int = 7981379
is_graduated: bool = True
gpa: float = 3.88

def to_string(student: str, major: str, student_number: int, is_graduated: bool, gpa: float) -> str:
    return "Student{Name: " + student + ", Major: " + major + ", Number: " + str(student_number) + ", Graduated: " + str(is_graduated) + ", GPA: " + str(gpa) + "}"

print("========== Student Description ==========")
print(f"Name\t\t: {student}")
print(f"Major\t\t: {major}")
print(f"Number\t\t: {student_number}")
print(f"Graduated\t: {is_graduated}")
print(f"GPA\t\t\t: {gpa}")

print(to_string(student, major, student_number, is_graduated, gpa))

student: str = "Balmond Kurniawan"
major: str = "Communication Science"
student_number: int = 3749034
is_graduated: bool = True
gpa: float = 3.51

print(to_string(student, major, student_number, is_graduated, gpa))


""" 
store multiple variable
"""
nilai1, nilai2, nilai3, nilai4 = 21, 22, 23, 24
print((nilai1 + nilai2 + nilai3 + nilai4) / 4)

""" 
pembulatan angka 
"""
using_abs = abs(-99)
using_round1 = round(22.5) 
using_round2 = round(456.56)
using_round3 = round(456.51)
print(f"Abs: {using_abs}, Round1: {using_round1}, Round2: {using_round2}, Round3: {using_round3}")
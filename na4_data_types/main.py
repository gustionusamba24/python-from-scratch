"""
STRING IN PYTHON
"""
string_1 = """
Sesuk
Prei
"""
print(string_1)

print("=====================")

# exclude newline pada bagian awal penulisan ''' atau """
string_2 = """\
Sesuk
Prei
"""
print(string_2)

""" 
None
"""
data_1 = "Simbada"
print(data_1)

data_2 = None
print(data_2)

data_3 = "Dokter"
print(data_3)

""" 
List in python: store collective value (mutable)
"""
list_1: list[int] = [23, 55, 87, 93]
print(list_1)

list_2: list[str] = ["alucard", "balmond", "cici"]
print(list_2)

list_3 = [24, True, "Bandung"]
print(list_3)
print(list_3[2])
print(list_3[0])

""" 
Tuple in python: store collective value (immutable)
"""
tuple_1 = (99, 54, 78, 12)
print(tuple_1)

tuple_2 = ("jogja", "bandung", "jakarta")
print(tuple_2)

print(tuple_1[3])
print(tuple_2[1])

""" 
Dictionary in python: store collective value in key value format
"""
student: dict[str, any] = {
    "name": "Harith",
    "number": 19112345,
    "major": "Computer Science",
    "is_graduated": False,
    "hobbies": ["gaming", "playing badminton"]
}

print(student)
print(student["major"])
print(student["is_graduated"])
print(student["name"])
print(student["hobbies"])
for hobby in student["hobbies"]:
    print(f"Hobby: {hobby}")

""" 
Set in python: store collective value. 
It has several disadvantages
- can't store the sequential of data
- can't change the existing element inside of it, but we can delete it
- can't access it using index (we surely can use looping)
"""
set_1 = {"apple", "pineapple", "papaya"}
print(set_1)
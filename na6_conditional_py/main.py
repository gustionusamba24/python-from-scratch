str_input = input("Enter your grade: ")
grade = int(str_input)
# print("inputan user:", str_input, type(grade))

if grade == 100:
    print("perfect")
elif grade >= 85:
    print("awesome")
elif grade >= 60:
    print("you passed the exam")

    if grade <= 70:
        print("you need to improve it")
    else:
        print("that was ok")
else:
    print("below the passing exam")

# Ternary
print("passed the exam") if grade >= 65 else print("below the passing grade")
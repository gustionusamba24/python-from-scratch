"""
    Global variable adalah variable yang dideklarasikan di root (tidak dalam suatu blok fungsi). Sedangkan local variable adalah yang dideklarasikan di dalam suatu block dan hanya di-block tersebut saja.
"""

name = "Cristiano Ronaldo"
print("greetings:", name)

def greet():
    today = "Thursday"
    print("happy", today, name)

if name:
    greet()
    greet_message = "have a good day"
    print("hello", name, greet_message)
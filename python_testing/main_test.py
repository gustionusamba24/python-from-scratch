from main import *

run_cases = [
    ("1", "10", "1010", (1, 2, 10)),
    ("101", "11", "10100", (5, 3, 20)),
    ("111", "1011", "11010", (7, 11, 26)),
]

def test(input1, input2, input3, expected):
    print("=================================")
    print(f"Inputs: {input1}, {input2}, {input3}")
    result = binary_string_to_int(input1, input2, input3)
    print(f"Expected: {expected}")
    print(f"Actual: {result}")
    
    if result == expected:
        print("Pass")
        return True

    print("Fail")
    return False

def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("All test cases passed!")
    else:
        print(f"{passed} test cases passed, {failed} test cases failed.")

test_cases = run_cases
main()
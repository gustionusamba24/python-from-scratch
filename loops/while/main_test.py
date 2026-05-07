from main import *

run_cases = [
    (0, 10, 20, 9), 
    (0, 10, 4, 1), 
    (8, 10, 20, 10)
]

def test(input1, input2, input3, expected):
    print("=================================")
    print("Inputs:")
    print(f" * current_health: {input1}")
    print(f" *     max_health: {input2}")
    print(f" * enemy_distance: {input3}")
    print(f"  Expected Health: {expected}")
    result = regenerate(input1, input2, input3)
    print(f"    Actual Health: {result}")
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
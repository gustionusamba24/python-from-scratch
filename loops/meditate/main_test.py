from main import *

run_cases = [
    (0, 10, 9, [9, 0]),
    (0, 12, 20, [12, 8]),
    (100, 100, 0, [100, 0]),
    (1, 100, 80, [81, 0]),
]

submit_cases = run_cases + [
    (0, 0, 0, [0, 0]),
    (1000, 1000, 5, [1000, 5]),
    (0, 10, 5, [5, 0]),
    (5, 2000, 500, [505, 0]),
]


def test(input1, input2, input3, expected):
    print("====================================")
    print("Inputs:")
    print(f" *         mana: {input1}")
    print(f" *     max_mana: {input2}")
    print(f" *  num_potions: {input3}")
    result = meditate(input1, input2, input3)
    result_mana = None
    result_potions = None
    if result is not None:
        result_potions, result_mana = result
    print(f"Expected: mana {expected[0]}, num_potions {expected[1]}")
    print(f"Actual:   mana {result_mana}, num_potions {result_potions}")
    if result_mana == expected[0] and result_potions == expected[1]:
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
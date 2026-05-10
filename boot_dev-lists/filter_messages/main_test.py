from main import filter_messages

TestCase = tuple[list[str], list[str], list[int]]

run_cases: list[TestCase] = [
    (
        ["darn it", "this dang thing won't work", "lets fight one on one"],
        ["darn it", "this thing won't work", "lets fight one on one"],
        [0, 1, 0],
    ),
    (
        [
            "well dang it",
            "dang the whole dang thing",
            "kill that knight, dang it",
            "get him!",
            "donkey kong",
            "oh come on, get them",
            "run away from the dang baddies",
        ],
        [
            "well it",
            "the whole thing",
            "kill that knight, it",
            "get him!",
            "donkey kong",
            "oh come on, get them",
            "run away from the baddies",
        ],
        [1, 2, 1, 0, 0, 0, 1],
    ),
    
]

def test(input: list[str], expected_filtered: list[str], expected_counts: list[int]) -> bool:
    print("============================================================")
    print("Input:")
    print(f" *             messages: {input}")
    print("Expected:")
    print(f" *    filtered messages: {expected_filtered}")
    print(f" * filtered dangs count: {expected_counts}")
    print("Actual:")
    try:
        result = filter_messages(input)
        print(f" *    filtered messages: {result[0]}")
        print(f" * filtered dangs count: {result[1]}")
    except Exception as e:
        print(f"Error: {e}")
        print("Fail")
        return False

    if result == (expected_filtered, expected_counts):
        print("Pass")
        return True

    print("Fail")
    return False

def main() -> None:
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1

    if failed == 0:
        print(f"All {passed} test cases passed!")
    else:        
        print(f"{passed} test cases passed, {failed} test cases failed.")

test_cases: list[TestCase] = run_cases

main()

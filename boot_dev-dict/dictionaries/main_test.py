from main import get_character_record

run_cases = [
    (
        "bloodwarrior123",
        "server1",
        5,
        1,
        {
            "name": "bloodwarrior123",
            "server": "server1",
            "level": 5,
            "rank": 1,
            "id": "bloodwarrior123#server1",
        },
    ),
    (
        "fronzenboi",
        "server2",
        2,
        1,
        {
            "name": "fronzenboi",
            "server": "server2",
            "level": 2,
            "rank": 1,
            "id": "fronzenboi#server2",
        },
    ),
]

def test(name, server, level, rank, expected_output):
    try:
        result = get_character_record(name, server, level, rank)
        for key, value in expected_output.items():
            print(f"Expected: {key}: {value}")
            print(f"Actual: {key}: {result[key]}\n")
            if result[key] != value:
                if type(result[key] != type(value)):
                    print(f"'{key}' values are different types!")
                    print(f"Expected '{key}' to be of type {type(value).__name__}, but got {type(result[key]).__name__}")
                print("Fail")
                return False
        if result != expected_output:
            print("Result object is incorrect:")
            for key, value in result.items():
                print(f" * {key}: {value}")
            print("Fail")
            return False
        print("Pass")
        return True
    except Exception as e:
        print(f"Exception: {str(e)}")
        print("Fail")
        return False

def main() -> None:
    index = 0
    passed = 0
    failed = 0
    for test_case in test_cases:
        index += 1
        print("============================")
        print(f"Test Case #{index}\n")
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1

    if failed == 0:
        print(f"{passed} test cases passed")
        print("All test cases passed")
    else:
        print(f"{passed} test cases passed, {failed} test cases failed")
        

test_cases = run_cases
main()
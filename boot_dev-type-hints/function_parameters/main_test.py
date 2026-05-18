from main import get_character_status

TestCases = tuple[str, int, float, bool, str]

run_cases: list[TestCases] = [
    (
        "Gandalf",
        80,
        99.5,
        True,
        "Gandalf is level 80 with 99.5 HP, and can cast spells",
    ),
    (
        "Frodo",
        12,
        24.0,
        False,
        "Frodo is level 12 with 24.0 HP, and cannot cast spells",
    ),
    (
        "Aragorn",
        45,
        82.5,
        False,
        "Aragorn is level 45 with 82.5 HP, and cannot cast spells",
    ),
]

expected_annotations: dict[str, type] = {
    "name": str,
    "level": int,
    "health": float,
    "has_magic": bool,
}

def test(
    char_name: str,
    char_level: int,
    char_health: float,
    has_magic: bool,
    expected_status: str,
) -> bool:
    print("===============================================")
    print(f"Inputs: {char_name}, {char_level}, {char_health}, {has_magic}")
    print()

    actual_status = get_character_status(char_name, char_level, char_health, has_magic)

    print(f"Expected status: {expected_status}")
    print(f"Actual status  : {actual_status}")
    print()

    if actual_status != expected_status:
        print("Fail")
        return False

    for param_name, expected_type in expected_annotations.items():
        actual_type = get_character_status.__annotations__.get(param_name)
        print(f"actual type: {actual_type}")

        print(f"{param_name}: expected {expected_type.__name__}")
        print(f"{param_name}: actual {getattr(actual_type, "__name__", None)}")
        print(f"getattr: {getattr(actual_type, "__name__", None)}")
        print()

        if actual_type is not expected_type:
            print("Fail")
            return False

        print("Pass")
        return True

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
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")

test_cases: list[TestCases] = run_cases

main()
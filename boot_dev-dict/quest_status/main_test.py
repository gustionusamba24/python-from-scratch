import json
from typing import TypedDict

from main import get_quest_status

class CharacterProgress(TypedDict):
    character_name: str
    quests: dict[str, dict[str, str]]

TestCase = tuple[CharacterProgress, str]

run_cases: list[TestCase] = [
    (
        {
            "character_name": "Sir Galahad",
            "quests": {
                "bridge_run": {
                    "status": "In Progress",
                },
                "talk_to_syl": {
                    "status": "Completed",
                },
            },
        },
        "In Progress"
    ),
    (
        {
            "character_name": "Lady Gwen",
            "quests": {
                "bridge_run": {
                    "status": "Completed",
                },
                "talk_to_syl": {
                    "status": "In Progress",
                },
            },
        },
        "Completed"
    ),
]

def test(progress: CharacterProgress, expected: str) -> bool:
    print("====================================")
    print("Inputs:")
    print(f" * Progress Dictionary: {json.dumps(progress, indent=4)}")
    print(f"Expected: {expected}")
    result = get_quest_status(progress)
    print(f"Actual: {result}")
    if result == expected:
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
        print(f"{passed} test cases passed")
        print("All test cases passed")
    else:
        print(f"{passed} test cases passed, {failed} test cases failed")

test_cases = run_cases
main()

# TODO
# Add `str` to name
# Add `int` to level
# Add `float` to health
# Add `bool` to has_magic

def get_character_status(name: str, level: int, health: float, has_magic: bool) -> str:
    status = f"{name} is level {level} with {health} HP"

    if has_magic:
        status += ", and can cast spells"
    else:
        status += ", and cannot cast spells"

    return status
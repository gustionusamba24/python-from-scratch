"""
    Keyword try except
    - tempatkan statement (yang berpotensi memunculkan exception) ke dalam block try
    - tambahkan block except dimana isinya adalah handler ketika exception muncul
"""


def calculate_bananan_distribution():
    try:
        total_banana = int(input("total banana: "))
        total_people = int(input("total people: "))
        res = total_banana // total_people
    except ValueError as err:
        print(f"the input should be integer. {err}")
    except ZeroDivisionError as err:
        print(f"unable to distribute banana because there is no person available. {err}")
    else:
        print(f"in fair distribution, each person should receive {res} banana")
    finally:
        print(f"program finished")


print("1st calculation")
calculate_bananan_distribution()

print("2nd calculation")
calculate_bananan_distribution()

print("3rd calculation")
calculate_bananan_distribution()

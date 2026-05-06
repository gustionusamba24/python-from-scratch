can_create_guild = 0b1000 # 8
can_review_guild = 0b0100 # 4
can_delete_guild = 0b0010 # 2
can_edit_guild = 0b0001 # 1

"""
    BITWISE `&` OPERATOR
"""
print("BITWISE `&` OPERATOR")
def get_create_bits(user_permissions):
    return can_create_guild & user_permissions


def get_review_bits(user_permissions):
    return can_review_guild & user_permissions


def get_delete_bits(user_permissions):
    return can_delete_guild & user_permissions


def get_edit_bits(user_permissions):
    return can_edit_guild & user_permissions


user_permissions_1 = 0b1010 # 1010 & 1000 = 1000
user_permissions_2 = 0b1001 # 1001 & 0100 = 0000
user_permissions_3 = 0b0110 # 0110 & 0010 = 0010
user_permissions_4 = 0b1110 # 1110 & 0001 = 0000

print(f"user_permissions_1: {user_permissions_1:b}, create: {get_create_bits(user_permissions_1)}, binary: {get_create_bits(user_permissions_1):b}")
print(f"user_permissions_2: {user_permissions_2:b}, review: {get_review_bits(user_permissions_2)}, binary: {get_review_bits(user_permissions_2):b}")
print(f"user_permissions_3: {user_permissions_3:b}, delete: {get_delete_bits(user_permissions_3)}, binary: {get_delete_bits(user_permissions_3):b}")
print(f"user_permissions_4: {user_permissions_4:b}, edit: {get_edit_bits(user_permissions_4)}, binary: {get_edit_bits(user_permissions_4):b}")

print("\nBITWISE `|` OPERATOR")
"""
    BITWISE `|` OPERATOR
"""
def calculate(glorfindel, galadriel, elendil, elrond):
    return glorfindel | galadriel | elendil | elrond

run_cases = [
    (0b0001, 0b0010, 0b0001, 0b1011)
]

for glorfindel, galadriel, elendil, elrond in run_cases:
    print(f"glorfindel: {glorfindel}, galadriel: {galadriel}, elendil: {elendil}, elrond: {elrond} => result: {calculate(glorfindel, galadriel, elendil, elrond)}")

num = int("100", 2) # it will be considered as string, but we convert it to integer with base 2 (binary)
print(f"num: {num}")

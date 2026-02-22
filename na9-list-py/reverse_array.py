# membalik urutan element list dengan cara manual

def print_array(length: int) -> list[int]:
    new_array: list[int] = []

    # while length > 0:
    #     number = int(input("Masukkan angka: "))
    #     new_array.append(number)
    #
    #     length -= 1

    for i in range(0, length):
        statement = f"masukkan angka ke-{i + 1}: "
        number = int(input(statement))
        new_array.append(number)

    return new_array


def reverse_array(array: list[int]) -> list[int]:
    copy_of_array = array.copy()

    max_index = len(array) - 1
    half_length = len(array) // 2

    for i in range(0, half_length):
        temp = copy_of_array[i]
        copy_of_array[i] = copy_of_array[max_index - i]
        copy_of_array[max_index - i] = temp

    return copy_of_array


original_array = print_array(5)
reversed_array = reverse_array(original_array)

print("Original array:", original_array)
print("Reversed array:", reversed_array)

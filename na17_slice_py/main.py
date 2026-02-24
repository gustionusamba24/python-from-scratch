"""
    Slicing adalah teknik untuk mengakses sekumpulan elemen/item dari data sequence sesuai dengan index yang diinginkan. Data sequence sendiri adalah klasifikasi tipe data yang berisi kumpulan data terueut atau sekuensial. Yang termasuk tipe data sequence adalah list, range, tuple, dan string.
"""

# Fungsi slice()
data_list = [2, 4, 6, 7, 9, 11, 13]
print(data_list)

list1 = data_list[2:6:1]
print(list1)

list2 = data_list[slice(2, 6, 1)]
print(list2)

sl = slice(2, 6)
list3 = data_list[sl]
print(list3)
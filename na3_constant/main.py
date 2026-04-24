from typing import Final

# KONVENSI PENULISAN KONSTANTA di PYTHON: Harus menggunakan huruf KAPITAL
PI: Final = 3.14
print("pi: %f" % PI)

GENDER: Final = "man"
print(f"Gender : {GENDER}")

# tipe konstanta TOTAL_MONTH ditentukan secara eksplisit yaitu `int`
TOTAL_MONTH: Final[int] = 12
print(f"total month: {TOTAL_MONTH}")
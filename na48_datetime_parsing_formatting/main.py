"""
    Parsing datetime
    Via datetime.strptime() dan kode format
    Class method datetime.strptime() digunakan untuk parsing string ke datetime dalam kombinasi kode format tertentu.
"""
# Contoh implementasinya seperti ini:
from datetime import datetime

date_string = "1985-04-12 23:20:50"
format_string = "%Y-%m-%d %H:%M:%S"

data_datetime = datetime.strptime(date_string, format_string)
print("datetime:", data_datetime)

date_string = '1985-04-12T23:20:50.52+0700'
format_string = '%Y-%m-%dT%H:%M:%S.%f%z'

data_datetime = datetime.strptime(date_string, format_string)
print("datetime:", data_datetime)

"""
    Via datetime.fromisoformat() terhadap data ISO Date Time (ISO 8601)
    untuk data waktu berbentuk string sesuai spesifikasi ISO Date Time atau ISO 8601, konversi ke bentuk datetime bisa dilakukan secara praktis menggunakan datetime.fromisoformat().
"""
# data_datetime = datetime.fromisoformat("1985-04-12T23:20:50.52")
# print("datetime:", data_datetime)
# # output ➜ datetime: 1985-04-12 23:20:50.520000
#
# data_datetime = datetime.fromisoformat("1985-04-12T23:20:50.52+0700")
# print("datetime:", data_datetime)
# output ➜ datetime: 1985-04-12 23:20:50.520000+07:00

"""
    Via datetime.fromtimestamp() terhadap data UNIX timestamp
    Data dengan format UNIX timestamp 10 digit bisa dikonversi ke bentuk datetime menggunakan method fromtimestamp()
"""
data_datetime = datetime.fromtimestamp(1702980333)
print("datetime:", data_datetime)

data_datetime = datetime.fromtimestamp(1702980333.244)
print("datetime:", data_datetime)
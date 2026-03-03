"""
    Python menyediakan package datetime berisi banyak sekali API untuk keperluan operasi data yang berhubungan dengan tanggal dan waktu.
"""
# Tipe data class date untuk penyimpanan informasi tanggal
from datetime import date, time, datetime
from dateutil import tz

data_date = date(year=2026, month=3, day=3)

print("date:", data_date)
print(" -> year:", data_date.year)
print(" -> month:", data_date.month)
print(" -> day:", data_date.day)

# Tipe data class time untuk penyimpanan informasi waktu (jam, menit, detik)
data_time = time(hour=11, minute=19, second=56)

print("time:", data_time)
print(" -> hour:", data_time.hour)
print(" -> minute:", data_time.minute)
print(" -> second:", data_time.second)
print(" -> timezone:", data_time.tzinfo)

# Tipe data timezone digunakan untuk penyimpanan tanggal dan waktu
# data_datetime = datetime(year=2026, month=3, day=3, hour=11, minute=23, second=24)

# combining date and time menggunakan datetime.combine
data_datetime = datetime.combine(data_date, data_time)

print("datetime:", data_datetime)
print(" ➜ year:", data_datetime.year)
print(" ➜ month:", data_datetime.month)
print(" ➜ day:", data_datetime.day)
print(" ➜ hour:", data_datetime.hour)
print(" ➜ minute:", data_datetime.minute)
print(" ➜ second:", data_datetime.second)
print(" ➜ timezone:", data_datetime.tzinfo)

# Mengambil datetime hari ini / sekarang
data1 = datetime.now()
print("sekarang (datetime):", data1)

data2 = datetime.today()
print("sekarang (datetime):", data2)

data2 = date.today()
print("sekarang (date):", data2)

# Membuat data timezone New York atau EST (Eastern Time):
tzinfo = tz.gettz("America/New_York")
data_time = time(hour=11, minute=37, second=50, tzinfo=tzinfo)

print("time:", data_time)

print("timezone:", data_time.tzinfo)
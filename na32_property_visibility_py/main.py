"""
    Visibility atau privacy dalam konteks OOP merujuk pada penentuan apakah property (baik itu attribute atau method) dapat diakses secara public atau hanya bisa diakses dari dalam class (private).
"""

"""
    Python, dari segi API kode yang tersedia, sebenarnya tidak secara eksplisit mendukung implementasi visibility property instance class. Semua attribute dan method secara default bersifat public di Python.
    Meskipun demikian, ada beberapa praktik umum untuk menandai bahwa suatu method atau attribute adalah private. Salah satunya adalah menggunakan teknik name mangling, di mana nama attribute atau method ditulis dengan diawali 2 karakter underscore, misalnya __name, __list_items, dan sejenisnya.
    
    Penamaan tersebut tidak benar-benar membuat visibility/property menjadi private, melainkan hanya sebagai penanda saja. Property sendiri tetap bisa diakses secara publik.
"""

from models import company
from models import product

if __name__ == "__main__":
    data = []

    c1 = company.Company(name="Microsoft", products=[
        product.Product(name="Windows", category="Operating system"),
        product.Product(name="Office 365", category="Productivity software"),
    ])
    data.append(c1)

    c2 = company.Company(name="Mattel", products=[
        product.Product(name="Hot Wheels", category="Car toys"),
        product.Product(name="Uno", category="Card game")
    ])
    data.append(c2)

    for d in data:
        d.info()
#Praktikum 1 - Class dan Object
class Hero: 
    pass

# Proses penciptaan object
hero_1 = Hero() 
hero_2 = Hero() 

# Memberikan atribut baru name untuk masing-masing object.
hero_1.name = "goku"
hero_2.name = "Vegeta"

# Menambahkan atribut power ke object.
hero_1.power = 100
hero_2.power = 200

# Menampilkan nilai atribut name dari kedua object.
print(hero_1.name)
print(hero_2.name)  

# menampilkan atribut apa saja yang dimiliki object dalam bentuk dictionary (key = nama atribut, value = nilainya).
print(hero_1.__dict__) 

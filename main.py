from animal import Animal, Cat, Dog

my_cat = Cat("Kissakas")
my_dog = Dog("Rex")

neighbours_dog = Dog("Chilly")
neighbours_cat = Cat("Miisu")

my_dog.dog_sees(neighbours_dog)
my_dog.dog_sees(my_cat)

my_cat.cat_sees(my_dog)
my_cat.cat_sees(neighbours_cat)
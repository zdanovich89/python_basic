x = 2
if x == 25:
    print("Right")
else:
    print("Wrong")

cars = ["bmw", "vw", "seat", "honda", "dodge", "audi", "kia", "jeep"]
german_cars = ["bmw", "audi", "vw"]

for car in cars:
    if car in german_cars:
        print(car.title() + " is a German car")
    else:
        print(car.title() + " isn't German car")
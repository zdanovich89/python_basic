cars = ["bmw", "vw", "seat", "honda", "dodge"]

for car in cars:
    print(car.upper())

mynumber_list = list(range(0, 10))
print(mynumber_list)

mynumber_list.sort(reverse=True)
print(mynumber_list)

print("Max number is:" + str(max(mynumber_list)))
print("Min number is:" + str(min (mynumber_list)))
print("Sum of list is:" + str(sum(mynumber_list)))

mycars = cars[:]
print(mycars)
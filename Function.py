

def show_greetings(name):
    print("Hello " + name)

def sum(x, y):
    print(x + y)


def factorial(x):
    value = 1
    for num in range(1, x + 1):
        value = value * num
    return value


show_greetings("Kent")
sum(10, 25)
for i in range(1, 10):
    print(str(i) + "!\t = " + str(factorial(i)))


def create_record(name, telephone, country):
    """Create Record"""
    record = {
        'name': name,
        'phone': telephone,
        'country': country
    }
    return record


user1 = create_record("John", "+54655656565", "Botswana")
user2 = create_record("Tommy", "645656565", "China")

print(user1)
print(user2)


def give_award(medal, *persons):
    """Give medals to persons"""
    for person in persons:
        print("Her " + person.title() + " get medal: " + medal)


give_award("For pretty", "Don", "Egi", "Chocolate")
name = "vaSIa champ"
print(name.title())
print(name.upper())
print(name.lower())

print("Hello 1\nHello 2")
print("List:\n\tPoint #1\n\tPoint #2\n\tPoint #3")
a = "...   mama kolia   ...."
a = a.strip(".").strip()
print(a)

enter = input('Enter your name: ')
enter2 = input('Enter language: ')
string = 'Hello {0}, I am {1}'.format(enter, enter2)
print(string)
enter2 = input('Enter your name again: ')
string2 = f'Hello {enter2}, I can do it in f-string {len(enter2)}'
print(string2)
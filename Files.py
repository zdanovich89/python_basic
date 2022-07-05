inputfile = "../book.txt"
outputfile = "../new_generate.txt"

key_word = "tiger"

myfile1 = open(inputfile, mode='r', encoding='latin_1')
myfile2 = open(outputfile, mode='a', encoding='latin_1')

for num, line in enumerate(myfile1, 1):
    if key_word in line:
        print("Line # " + str(num) + ": " + line.strip())
        myfile2.write(line)

myfile1.close()
myfile2.close()
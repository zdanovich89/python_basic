import re


my_text = "Baxter Love,(756) 439-8627,aliquam.arcu@protonmail.couk,United Kingdom"\
          "Logan Dickerson,(696) 131-0566,malesuada.integer@protonmail.net,Ireland"\
          "Camilla Whitney,1-344-508-3320,felis.ullamcorper@google.edu,United Kingdom"\
          "Elmo Wooten,1-474-336-3717,ut.erat.sed@hotmail.net,Belgium"\
          "Mark Montoya,1-671-268-2936,felis.ullamcorper.viverra@aol.org,Costa Rica"


text_look_for = r"\d+\D\d+\D\d+\D\d+"
all_results = re.findall(text_look_for, my_text)

print(all_results)

input_file_name = "../data.txt"
result_file_name = "../result.txt"

input_file = open(input_file_name, mode='r')
result_file = open(result_file_name, mode='w')
my_text = input_file.read()

look_for = r"[\w.-]+@[\w-]+\.[\w.]+"

results = re.findall(look_for, my_text)

for item in results:
    print(item)
    result_file.write(item + "\n")

print("Total: " + str(len(results)))
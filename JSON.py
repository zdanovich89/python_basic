import json

file_name = "user_settings.txt"
my_file = open(file_name, mode='w', encoding='latin_1')

player_1 = {
    'Player_Name': "Donny",
    'Score': 100,
    'Awards': ["Keks", "Ice", "Snow"]
}

player_2 = {
    'Player_Name': "Penny",
    'Score': 99,
    'Awards': ["Keks", "Milk", "Pyz"]
}


my_players = []
my_players.append(player_1)
my_players.append(player_2)

  # -----------SAVE TO JSON---------

json.dump(my_players, my_file)
my_file.close()

  # -----------LOAD by JSON---------

my_file = open(file_name, mode='r', encoding="latin_1")
json_data = json.load(my_file)

for user in json_data:
    print("Player Name is: " + str(user['Player_Name']))
    print("Player Score is: " + str(user["Score"]))
    print("Player Award #1: " + str(user["Awards"][0]))
    print("Player Award #2: " + str(user["Awards"][1]))
    print("Player Award #3: " + str(user["Awards"][2]))
    print("------------------------\n")

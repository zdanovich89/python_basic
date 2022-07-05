enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Keks'
}

print(enemy)

print("Location X = " + str(enemy['loc_x']))
print("Location Y = " + str(enemy['loc_y']))
print("His name is: " + enemy['name'])

enemy['rank'] = 'Admiral'
print(enemy)

del enemy['rank']
print(enemy)

enemy['loc_y'] = enemy['loc_y'] + 50
enemy['health'] = enemy['health'] - 50
if enemy['health'] < 70:
    enemy['color'] = 'yellow'

print(enemy)
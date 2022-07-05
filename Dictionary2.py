enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Keks'
}

all_enemies = []

for x in range(0, 10):
    all_enemies.append(enemy.copy())

for enem in all_enemies:
    print(enem)

all_enemies[9]['health'] = 30

for enem in all_enemies:
    print(enem)
def tower_builder(n_floors):
        floors = []
        for i in range(n_floors):
            n_floors -= 1
            floors.append(' ' * n + '*' * (i * 2 + 1) + ' ' * n)

        return floors

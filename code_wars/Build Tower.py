def tower_builder(n_floors):
        floors = []
        n = n_floors
        for i in range(n_floors):
            n -= 1
            floors.append(' ' * n + '*' * (i * 2 + 1) + ' ' * n)

        return floors
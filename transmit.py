def gridlandMetro(n, m, k, track):
    rest = {}
    occupied = 0
    for t in track:
        if t[0] in rest:
            rest[t[0]].append([t[1], t[2]])
        else:
            rest[t[0]] = [[t[1], t[2]]]

    for _, val in rest.items():
        val.sort()

        occupied += val[-1] - val[0] + 1

    return m*n - occupied
def graph():
    gra = {}
    n = int(input('Введите кол-во вершин: '))
    for i in range(n):
        s = []
        v = (input('Введите название вершины: '))
        s += (input('Введите связанные с ней вершины: ').split())
        print()
        gra[v] = s
    main(gra)


def main(g):
    s = str(input('Введите вершину старта: '))
    e = str(input('Введите вершину конца: '))
    print()
    a = int(input('1. Вывести случаный путь\n2. Вывести все пути\n3. Вывести кратчайший путь\n4. Выход из программы\n'))
    if a == 1:
        print()
        print(find_way(g, s, e))
        main(g)
    elif a == 2:
        print()
        print(all_ways(g, s, e))
        main(g)
    elif a == 3:
        print()
        print(shortest_way(g, s, e))
        main(g)
    if a == 4:
        print()
        exit()


def find_way(g, start, end, way=[]):
    way = way + [start]
    if start == end:
        return way
    if not (start in g):
        return None
    for n in g[start]:
        if n not in way:
            newway = find_way(g, n, end, way)
            if newway:
                return newway
    return None


def all_ways(g, start, end, way=[]):
    way = way + [start]
    if start == end:
        return [way]
    if not (start in g):
        return []
    ways = []
    for n in g[start]:
        if n not in way:
            newways = all_ways(g, n, end, way)
            for newway in newways:
                ways.append(newway)
    return ways


def shortest_way(g, start, end, way=[]):
    way = way + [start]
    if start == end:
        return way
    if not (start in g):
        return None
    shortest = None
    for n in g[start]:
        if n not in way:
            newway = shortest_way(g, n, end, way)
            if newway:
                if not shortest or len(newway) < len(shortest):
                    shortest = newway
    return shortest


graph()
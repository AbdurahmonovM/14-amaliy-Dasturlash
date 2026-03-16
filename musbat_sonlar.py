def filtr(sonlar):
    yangi = []
    for son in sonlar:
        if son > 0:
            yangi.append(son)
    return yangi


if __name__ == "__main__":
    print(filtr([1, -2, 3, -4, 5]))

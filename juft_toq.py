def juftmi(son):
    if son % 2 == 0:
        return "Juft"
    else:
        return "Toq"


if __name__ == "__main__":
    son = int(input("Son kiriting: "))
    print("Natija:", juftmi(son))

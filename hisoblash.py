def hisobla(a, b, amal):
    if amal == "+":
        return a + b
    elif amal == "-":
        return a - b
    elif amal == "*":
        return a * b
    elif amal == "/":
        if b != 0:
            return a / b
        else:
            return "0 ga bo‘lish mumkin emas"
    else:
        return "Noto‘g‘ri amal"


if __name__ == "__main__":
    a = float(input("1-sonni kiriting: "))
    b = float(input("2-sonni kiriting: "))
    amal = input("Amalni kiriting (+, -, *, /): ")
    print("Natija:", hisobla(a, b, amal))

def orta(sonlar):
    if len(sonlar) == 0:
        return 0
    else:
        return sum(sonlar) / len(sonlar)


if __name__ == "__main__":
    sonlar = list(map(float, input("Sonlarni probel bilan kiriting: ").split()))
    print("O‘rtacha qiymat:", orta(sonlar))

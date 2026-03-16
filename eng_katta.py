def top(sonlar):
    if len(sonlar) == 0:
        return None
    else:
        return max(sonlar)


if __name__ == "__main__":
    sonlar = list(map(float, input("Sonlarni probel bilan kiriting: ").split()))
    print("Eng katta son:", top(sonlar))

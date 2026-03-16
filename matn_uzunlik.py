def uzunlik(matn):
    if matn == "":
        return "Bo‘sh matn"
    else:
        return len(matn)


if __name__ == "__main__":
    print(uzunlik("Salom"))
    print(uzunlik(""))

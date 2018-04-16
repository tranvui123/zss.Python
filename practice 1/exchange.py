def exchange(money):
    usd = 57
    euro = 60
    vnd = 0.25
    currency = int(input("Укажите код валюты(Доллары - 400. Евро - 401, Донг Вьетнама - 402): "))

    if currency == 400:
        cache = round(money / usd, 2)
        print("вылюта: Доллары США ")
    elif currency == 401:
        cache = round(money / euro, 2)
        print("вылюта: Евро")
    elif currency == 402:
        cache = round(money / vnd, 2)
        print("вылюта: Донг Вьетнама")
    else:
        cache = 0
        print("Неизвестная валюта")
    print("к получению: ", cache)


def main():
    money = int(input("введите сумму, которую вы хотите обменять: "))
    exchange(money)


if __name__ == "__main__":
    main()
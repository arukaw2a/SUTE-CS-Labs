def main() -> None:
    a = 0
    b = 0

    while 100 > abs(a) or abs(a) > 999:
        try:
            a = int(input("Введіть перше тризначне число -> "))
        except ValueError as ve:
            print(ve)
    while 100 > abs(b) or abs(b) > 999:
        try:
            b = int(input("Введіть друге тризначне число -> "))
        except ValueError as ve:
            print(ve)

    print(f"Сума: {int(str(a)[-1]) + int(str(b)[-1])}")
    print(f"Добуток: {int(str(a)[-1]) * int(str(b)[-1])}")

if __name__ == "__main__":
    main()
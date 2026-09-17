import sys

def main() -> None:
    try:
        n = int(sys.argv[1])
    except ValueError as ve:
        print(ve)

    if n < 3:
        print("Багатокутник повинен мати 3, або більше кутів")
        return

    angle = (n - 2) * 180 / n

    print(f"Кут = {angle}°")

if __name__ == "__main__":
    main()
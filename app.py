from utils import add, subtract

def main():
    print("Calculator")
    print("1. Add")
    print("2. Subtract")

    choice = input("Choose: ")

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtract(a, b))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
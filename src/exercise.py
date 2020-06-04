def main():
    #write your code below this line

    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))

    if num1 > num2:
        print(f"{num1} is greater than {num2}.")
    elif num1 < num2:
        print(f"{num1} is smaller than {num2}.")
    else:
        print(f"{num1} is equal to {num2}.")

if __name__ == '__main__':
    main()

def print_factor(number):
    print(f"the factors of {number} is: ")
    for i in range (1, number + 1):
        if number % i == 0:
            print(i)
number=int(input("enter a number to check: "))
print_factor(number)
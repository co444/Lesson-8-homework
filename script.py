def rearrange_numbers(a, b, c, option):
    if option == 1:
        return b, c, a
    elif option == 2:
        return c, a, b
    elif option == 3:
        return c, b, a  
    elif option == 4:
        return a, b, c  
    else:
        print("Invalid choice! Keeping original order.")
        return a, b, c

print("Enter three numbers:")
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))

print("\nChoose an arrangement:")
print("1 - Rotate Left (a → b, b → c, c → a)")
print("2 - Rotate Right (a → c, b → a, c → b)")
print("3 - Reverse (a → c, b → b, c → a)")
print("4 - No change")

choice = int(input("Enter your choice (1-4): "))

num1, num2, num3 = rearrange_numbers(num1, num2, num3, choice)

print("\nAfter rearrangement:")
print("First number:", num1)
print("Second number:", num2)
print("Third number:", num3)
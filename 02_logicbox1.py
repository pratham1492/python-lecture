print("Welcome to the pattern generator and number analyzer!")

print("n Select and options:")
print("1. Pattern Generation (Right-angled triangle)")
print("2. Number Analysis")
print("3. Exit")

while True:
    choice = input("Enter your options (1-3): ")

    if choice == "1":
        # Pattern Generation Code Here
        rows = int(input("Enter number of rows: "))
        if rows <= 0:
            print("Invalid row count! Must be positive.")
            break
        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end="")
            print()

    elif choice == "2":
        # Number Analysis Code Here
        start = int(input("Enter start number: "))
        end = int(input("Enter end number: "))
        if start > end:
            print("Invalid range! Start must be <= End.")
            break
        total_sum = 0
        for num in range(start, end + 1):
            if num % 2 == 0:
                print(num, "is Even")
            else:
                print(num, "is Odd")
            total_sum += num
        print("Sum of all numbers:", total_sum)

    elif choice == "3":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

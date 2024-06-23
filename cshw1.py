import math
import time
import os

def sqrt_numbers(numbers):
    return [math.sqrt(x) for x in numbers]

def average_numbers(numbers):
    return sum(numbers) / len(numbers)

def reverse_numbers(numbers):
    return numbers[::-1]

def insert_number(numbers, num):
    numbers.append(num)
    return numbers

def delete_number(numbers, num):
    if num in numbers:
        numbers.remove(num)
    return numbers

def delete_all_numbers(numbers):
    numbers.clear()
    return numbers

def animate_loading():
    animations = ["-", "\\", "|", "/"]
    for i in range(10):
        print("Loading", animations[i % 4], end="\r")
        time.sleep(0.2)
    print("Loaded!")

def main():
    numbers = []
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "="*40)
        print("          **NUMBER OPERATIONS MENU**          ")
        print("="*40)
        print(" 1. **Enter numbers**")
        print(" 2. **Calculate SQRT**")
        print(" 3. **Calculate Average**")
        print(" 4. **Reverse numbers**")
        print(" 5. **Insert number**")
        print(" 6. **Delete number**")
        print(" 7. **Delete all numbers**")
        print(" 8. **View numbers**")
        print(" 9. **Exit**")
        print("="*40)
        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            n = int(input("Enter the number of integers: "))
            numbers = []
            for i in range(n):
                while True:
                    num = int(input(f"Enter integer {i+1}: "))
                    if num > 0:
                        numbers.append(num)
                        break
                    else:
                        print("Please enter a positive integer.")
            print("Numbers entered:", numbers)
            time.sleep(2)

        elif choice == "2":
            if numbers:
                animate_loading()
                sqrt_result = sqrt_numbers(numbers)
                print("SQRT of numbers:", sqrt_result)
                input("Press Enter to continue...")
            else:
                print("Please enter numbers first.")
                input("Press Enter to continue...")

        elif choice == "3":
            if numbers:
                animate_loading()
                avg_result = average_numbers(numbers)
                print("Average of numbers:", avg_result)
                input("Press Enter to continue...")
            else:
                print("Please enter numbers first.")
                input("Press Enter to continue...")

        elif choice == "4":
            if numbers:
                animate_loading()
                reversed_numbers = reverse_numbers(numbers)
                print("Reversed numbers:", reversed_numbers)
                input("Press Enter to continue...")
            else:
                print("Please enter numbers first.")
                input("Press Enter to continue...")

        elif choice == "5":
            if numbers:
                while True:
                    num = int(input("Enter a number to insert: "))
                    if num > 0:
                        numbers = insert_number(numbers, num)
                        print("Updated numbers:", numbers)
                        break
                    else:
                        print("Please enter a positive integer.")
                input("Press Enter to continue...")
            else:
                print("Please enter numbers first.")
                input("Press Enter to continue...")

        elif choice == "6":
            if numbers:
                while True:
                    num = int(input("Enter a number to delete: "))
                    if num in numbers:
                        numbers = delete_number(numbers, num)
                        print("Updated numbers:", numbers)
                        break
                    else:
                        print("Number not found in the list.")
                input("Press Enter to continue...")
            else:
                print("Please enter numbers first.")
                input("Press Enter to continue...")

        elif choice == "7":
            if numbers:
                animate_loading()
                numbers = delete_all_numbers(numbers)
                print("All numbers deleted!")
                input("Press Enter to continue...")
            else:
                print("No numbers to delete.")
                input("Press Enter to continue...")

        elif choice == "8":
            if numbers:
                print("Current numbers:", numbers)
                input("Press Enter to continue...")
            else:
                print("No numbers entered yet.")
                input("Press Enter to continue...")

        elif choice == "9":
            print("Exiting the program. Goodbye!")
            time.sleep(2)
            break

        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
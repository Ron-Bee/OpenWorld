def binary_search(arr, target):
   
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1

def main():
    try:
        user_list = input("Enter a sorted list of numbers separated by spaces: ")
        numbers = [int(item) for item in user_list.split()]

        target = int(input("Enter the number to search for: "))

        result = binary_search(numbers, target)
        if result != -1:
            print(f"Number found at index: {result}")
        else:
            print("Number not found in the list.")

    except ValueError:
        print("Invalid input. Please enter only numbers.")

if __name__ == "__main__":
    main()
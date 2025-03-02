import random

def main():
    # Create an array with 5000 zeros and 5000 ones
    arr = [0] * 5000 + [1] * 5000

    random.shuffle(arr)
    #print(arr)
    

    target = 1  # Set the target value to search for
    tries = 0   # Counter for the number of attempts

    # Continue until the target is found
    while True:
        tries += 1

        # Randomly pick an index in the array
        index = random.randint(0, len(arr)-1)

        # Check if the element at the chosen index is the target
        if arr[index] == target:
            print(f"Index of the first {target} found:", index)
            print("Number of tries:", tries)
            break

if __name__ == "__main__":
    main()




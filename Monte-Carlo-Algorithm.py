import random

def main():
    # Generate an array with 5000 zeros and 5000 ones (total 10,000 elements)
    arr = [0] * 5000 + [1] * 5000

    # Shuffle the array to randomize the order of elements
    random.shuffle(arr)
    #print(arr)

    target = 1 # searching for element 1
    tries = 0 # Number of tries
    k = 3 # Maximum number of attempts

    # Attempt to find a 1 in at most k tries
    while tries < k:
        tries += 1
        
        index = random.randint(0, len(arr)-1)
        if arr[index] == target:
            print("Index of first 1 found: ", index)
            print("Number of tries:", tries)
            break
        
    else:
        # If the loop completes without a break, it means 1 was not found in k attempts
        print(f"Couldnt find {target} in {k} tries.")


if __name__ == "__main__":
    main()

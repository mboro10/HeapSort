import math

def heapify(mylist, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # If left child exists and is greater than root, account for NaN handling
    if left < n and (mylist[left] > mylist[largest] or (math.isnan(mylist[left]) and not math.isnan(mylist[largest]))):
        largest = left

    # If right child exists and is greater than largest so far, account for NaN handling
    if right < n and (mylist[right] > mylist[largest] or (math.isnan(mylist[right]) and not math.isnan(mylist[largest]))):
        largest = right

    # Change root if needed
    if largest != i:
        mylist[i], mylist[largest] = mylist[largest], mylist[i]  # Swap

        # Heapify the root
        heapify(mylist, n, largest)


def heapsort(mylist):
    n = len(mylist)
    
    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):  # Correct starting index
        heapify(mylist, n, i)  # Pass full heap size

    for i in range(n - 1, 0, -1):
        mylist[i], mylist[0] = mylist[0], mylist[i]  # Move current root to end
        heapify(mylist, i, 0)  # Decrease heap size after each swap


def printlist(mylist):
    for i in mylist:
        print(i, end=" ")
    print("\n")

if __name__ == "__main__":
    user_input = input("Enter space separated numbers: ")
    mylist = list(map(float, user_input.split()))  # Use float to handle NaN input as well

    print("Original list:")
    printlist(mylist)

    heapsort(mylist)

    print("Sorted list:")
    printlist(mylist)

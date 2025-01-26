def heapify(mylist, n, i):
    largest = i  # Start with the root as the largest
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # If the left child is larger than the root
    if left < n and mylist[left] > mylist[largest]:
        largest = left

    # If the right child is larger than the largest so far
    if right < n and mylist[right] > mylist[largest]:
        largest = right

    # If the largest is not root, swap and continue heapifying
    if largest != i:
        mylist[i], mylist[largest] = mylist[largest], mylist[i]
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
    mylist = list(map(int, user_input.split()))

    print("Original list:")
    printlist(mylist)

    heapsort(mylist)

    print("Sorted list:")
    printlist(mylist)

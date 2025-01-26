def heapify(mylist, n, i):
    max_, left, right = i, 2 * i + 1, 2 * i + 2
    
    if left <= n and mylist[left] > mylist[max_]: # Check if left child within bound and greater than current max
        max_ = left
    
    if right <= n and mylist[right] > mylist[max_]: # Check if right child within bound and greater than current max
        max_ = right
    
    if max_ != i: # swap and heapify, if largest not root
        mylist[i], mylist[max_] = mylist[max_], mylist[i]
        heapify(mylist, n, max_)

def heapsort(mylist):
    n = len(mylist)
    
    for i in range(n // 2, -1, -1):
        heapify(mylist, n - 1, i)
    
    for i in range(n - 1, -1, -1):
        mylist[i], mylist[0] = mylist[0], mylist[i]
        heapify(mylist, i - 1, 0)

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

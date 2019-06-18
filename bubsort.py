def BubbleSort(list1):
    for a in range(n):
        for  b in range(0, n-a-1):
            if list1[b]>list1[b+1]:
                list1[b], list1[b+1] = list1[b+1],list1[b]


n = int(input("Enter number of elements "))

list1 = []

print("Enter elements of list ")

for a in range(n):
    e = int(input())
    list1.append(e)

BubbleSort(list1)

print(list1)
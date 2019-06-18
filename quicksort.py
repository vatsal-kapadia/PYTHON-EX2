def part(l, h):
    pivot = list1[l]
    a = l + 1
    b = h - 1

    while True:
        while a <= b and list1[a] <= pivot:
            a = a + 1
        while a <= b and list1[b] >= pivot:
            b = b - 1

        if a <= b:
            list1[a], list1[b] = list1[b], list1[a]
        else:
            list1[l], list1[b] = list1[b], list1[l]
            return b

def quicksort(l,h):
    if l<h:
        b= part(l,h)
        quicksort(l,b)
        quicksort(b+1,h)


n = int(input("Enter number of elements "))

list1=[]

for a in range(n):
    ele= int(input())
    list1.append(ele)

l = 0
h = n

quicksort(l,h)

print(list1)
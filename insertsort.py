def insertsort(list1):
    for a in range(1,n):
        ce = list1[a]
        pos=a
        while ce<list1[pos-1] and pos>0:
            list1[pos], list1[pos-1] = list1[pos-1], list1[pos]
            pos=pos-1
            

n= int(input("Enter number of elements "))

print("Enter elements ")

list1=[]

for a in range(n):
    e=int(input())
    list1.append(e)
insertsort(list1)

print(list1)
def selsort(list1):
 for a in range(n): 
     mini = a
     for b in range(a+1, n): 
         if list1[mini] > list1[b]:
             mini = b
     list1[a],list1[mini]=list1[mini],list1[a]
     print(list1)

n = int(input("Enter number of elements "))  
list1 = [] 
print("Enter elements of list ")
for a in range(n):
    e = int(input())
    list1.append(e)
selsort(list1) 
print(list1)
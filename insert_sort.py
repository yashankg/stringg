
def insert_sort(list1, n):  

        for i in range(1, n):   
            value = list1[i]  
            j = i - 1  
            while j >= 0 and value < list1[j]:  
                list1[j + 1] = list1[j]  
                j -= 1  
            list1[j + 1] = value  
        print("The sorted list is : ",list1)  
list1=[23,56,7,12,28,34]
insert_sort(list1, len(list1))
'''  

list1 = []
n=int(input("Enter the number of elements in array : "))
for i in range (n):
	a=int(input("Enter element : "))
	list1.append(a)  
print("The unsorted list is : ",list1)  
insert_sort(list1)
#print("The sorted list1 is:", insertion_sort(list1))  
'''
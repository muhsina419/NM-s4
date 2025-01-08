def binary_search (arr , target):
	low=0;
	high=len(arr)-1
	
	while low<=high:
		mid=(low+high)//2
		if arr[mid]==target:
			return mid
		elif arr[mid]>target:
			high=mid-1
		else :
			low=mid+1
	return -1

target=int(input("Enter the search element : "))
arr=list(map(int, input("Enter the sorted array elements ").split()))
result=binary_search(arr,target)
if result != -1 :
	print(f"Element found at index {result}")
else:
	print("Element not found")
	

			

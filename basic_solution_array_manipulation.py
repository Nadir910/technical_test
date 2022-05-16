n,m=map(int,input().split())
updated_list=[0]*n
for _ in range(m):
	a,b,k=[int(n) for n in input().split()]
	for i in range(a-1,b):
		updated_list[i]+=k
	print("Updated list: ", updated_list)
print("Maximum value is: ", max(updated_list))
n,m=map(int,input().split())
updated_list=[0]*(n+1)
maximum_value=temporary_value=0
for _ in range(m):
	a,b,k=[int(n) for n in input().split()]
	updated_list[a-1]+=k
	if b<=n:
		updated_list[b]-=k
	print("Updated list: ", updated_list)
for i in updated_list:
	temporary_value+=i
	if maximum_value<temporary_value:
		maximum_value=temporary_value
print("Maximum value is: ", maximum_value)
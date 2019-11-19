sum1=0
sum2=0
N=int(input("Enter the number:"))
for i in range(1,N+1):
#Sum of squares of numbers
    sum1=sum1+i*i
#Sum of individual numbers
    sum2=sum2+i
sum2=sum2**2
diff=sum2-sum1
print(diff)

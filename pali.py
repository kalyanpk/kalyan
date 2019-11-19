def palindrome(N):
    for i in range(1,N+1):
        print (((10 ** i - 1) // 9) ** 2)
a=int(input("Enter the size of the palindrome:"))
palindrome(a)

def check_palindrome(l,n):
    i=0
    j=n-1
    while(i<=j):
        if(l[i]!=l[j]):
            return False
        else:
            i=i+1
            j=j-1
    return True
n=int(input())
l=[]
for i in range(n):
    s=input()
    l.append(s)
i=0
j=n-1
print(check_palindrome(l,n))

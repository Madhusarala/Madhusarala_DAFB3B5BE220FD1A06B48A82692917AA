#1.1 Implement a recursive function to calculate the factorial of a given number.
def fact_rec(n):
    if n==0 or n==1:
      return 1
    else:
      return n*fact_rec(n-1)
num=int(input("Enter a value:"))
res=fact_rec(num)
print ("The factorial of{} is {}.".format(num,res))


#V.1
number = int(input("Please enter only 4 digits whole number: "))
n1=number//1000
n2=number%1000//100
n3=number%100//10
n4=number%10
print(n1,n2,n3,n4, sep='\n')
#V.2
number = int(input("Please enter only 4 digits whole number: "))
n1,rest1=divmod(number,1000)
n2,rest2=divmod(rest1,100)
n3,n4=divmod(rest2,10)
print(n1,n2,n3,n4, sep='\n')
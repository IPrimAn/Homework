number = int(input("Please enter only 5 digits whole number to get inverse number: "))
n1=number//10000 #1
n2=number%10000//1000 #2
n3=number%1000//100 # 3
n4=number%100//10
n5=number%10
result=n5*10000+n4*1000+n3*100+n2*10+n1
print("This is your inverse number:", result)
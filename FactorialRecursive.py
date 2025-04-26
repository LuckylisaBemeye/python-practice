def factorial(num):
    if num==1:
        return num*1
    else:    
        return num* factorial(num-1)

    print(factorial)

x=int(input("Enter the number whose factorial you want: "))
result=factorial(x)        
print(x, "! = ",result)
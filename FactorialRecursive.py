def factorial(num):
    if num==1:
        return num*1  #base case
    else:    
        return num* factorial(num-1) #recursive case

    print(factorial)

x=int(input("Enter the number whose factorial you want: "))  #specifying the input is an integer rather than a string as the imput function defaults it to
result=factorial(x)        
print(x, "! = ",result)

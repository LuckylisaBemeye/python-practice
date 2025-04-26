def sumDig(number):
    i=0
    tow=0
    while i<len(number):
        
        tow+=int(number[i])
        i+=1
    return tow

num=input("Ënter any number: ")

sum=sumDig(num)    

print("The sum of the digits of given number: ", num," is: ", sum)


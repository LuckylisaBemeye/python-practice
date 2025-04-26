
def FactorialLoop(num):
    fact=1
    i=1
    while(i<=num):
        fact *= i
        i+=1 #incrementing the value of the program counter i
    print("The factorial of ", num," is : ",fact )    

FactorialLoop(int(input("Ënter any number: ")))

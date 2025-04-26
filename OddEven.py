

def checkNumType(num):
    if num%2==0: 
        print(num, "is even")
    else:   
        print(num," is odd")

checkNumType(int(input("Ënter any whole number: "))) #wrapping up the input function in the parentethes of int type caster inorder to ensure input is integer

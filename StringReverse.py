
def ReverseStr(string):
    string_Len=len(string)
    revString=['']*string_Len # Initializing a list with the same length as the input string
    #why a list? a list is immutable unlike a string whish is benefitial for my approach of coding

    i=string_Len-1
    while i>=0:
        m=i+1
        revString[string_Len-m]=string[i]
        i-=1

    reversed_string=''.join(revString) #coverting the list to a string so that the output is a string not a list 
    print(reversed_string)

name=str(input("ënter a string: "))
ReverseStr(name)
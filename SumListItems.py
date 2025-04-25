
numbers=[1,2,3,4,5,6]
sum=0;
def itemsSum():
    i=0
    while i<len(numbers):
        global sum  
        sum= sum+ numbers[i];
        i+=1
    print(sum); 

itemsSum()
    
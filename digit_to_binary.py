#Create variables that will help in code
i=0
a = int(input(": "))
copy_a=a
j = 0
#We find the exponent in the given number base of 2
def eksponenti():
    global i,a
    while a>=1:
        a=a/2
        i=i+1
#Create a blank list that will help us creating the binary number
number= []
#Expanding the list till the exponent
def lista():
    global number,j
    while j<i:
        number.append(0)
        j=j+1
#Create the number
def exhanger():
    global variable,j,eks,copy_a
    while copy_a>0:
        b=variable-j
        fuqia=2**eks
        if copy_a>=fuqia:
            copy_a=copy_a-fuqia
            number[b]=1
            j=j-1
            eks=eks-1
        else :
            number[b]=0
            eks = eks - 1
            j=j-1
eksponenti()
lista()
#Create a variable that will help us for array
variable=j
#create an exponent
eks=j-1
exhanger()
listToStr = ''.join([str(elem) for elem in number])
print(listToStr)





#******************************************************************************
#CPSC-51100, Summer2 2019
#Nisha George
#Programming Assignment #1
#******************************************************************************
 
#variable declaration and initialization
xnb = 0  #mean
sn2 = 0  #variance
n = 0    #number of values
#prompt user to enter a number
num = int(input('Enter a number: '))
    
#command to loop while number is positive
while (num >= 0):
    #store previous mean in new variable called previous_xnb
    previous_xnb = xnb
    #increment number of values
    n = n + 1
    #calculate updated mean
    xnb = xnb + (num-xnb)/n

    #if number of values is greater than 1, calculate variance
    if (n>1):            
        sn2 = ((n-2)/(n-1)) * sn2 + ((num - previous_xnb) ** 2)/n 
    print ("Mean is " + str(xnb) + " variance is " + str(sn2))
    #prompt user for another number
    num = int(input('Enter a number: '))
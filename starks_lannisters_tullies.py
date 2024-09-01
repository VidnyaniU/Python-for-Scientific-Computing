# Read two integers M and N from the user. They could be positive, negative or zero.  Run a for loop from M to N (including N). For every number i in the loop,  print one of the following messages: 
# if (i+1) is divisible by 3 and if (i-1) is divisible by 4 print "Starks"
# if (i+1) is even and if (i-1) is divisible by  5 print "Lannisters"
# For everything else print "Tullies"
# Count how many times you get each.

def print_and_count(M,N):
    starks = 0
    lannisters = 0
    tullies = 0

    for i in range (M,N+1):
        if(i+1)%3 ==0  and (i-1)%4 ==0:
            print(str(i) + " Starks")
            starks +=1

        elif (i+1)%2 ==0 and (i-1)%5 == 0:
            print(str(i) + " Lannisters") 
            lannisters += 1
        
        else:
            print(str(i) + " Tullies")
            tullies +=1
    return starks , lannisters , tullies

M = int(input("Enter the value of M :: "))
N = int(input("Enter the value of N :: "))

starks , lannisters , tullies = print_and_count(M, N)

print("Count of messages :: ")
print("Starks :: " + str(starks))
print("lannisters :: " + str(lannisters))
print("Tullies :: " + str(tullies))

# Write a program which will find all such numbers which are divisible by 7 
# but are not a multiple of 5 between 2000 and 3200 (both included).
#  The numbers obtained should be printed in a comma-separated sequence on a single line.
def mathematics():
    outputList = []
    for j in range(1000, 2000+1):
        if (j%7==0) and (j%5!=0):
            outputList.append(j)
    return outputList

print(mathematics())
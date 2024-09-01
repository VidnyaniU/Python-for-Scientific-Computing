# Write a program to find all possible pairs of numbers whose product is 1947. Store them as list of list. (eg: [[1,1947],[33,59]]) 
def find_pairs(product):
    pairs = []
    for i in range (1,int(product ** 0.5)+1):  #loop will go from 1 to sqrt of 1947
        if product % i ==0:
            pairs.append([i , product // i])
    return pairs

product = 1947
pairs= find_pairs(product)
print(pairs)
def has_dup(number):
    dups = []
    
    for x in range(0,5):
        tup = ()
        if number[x] == number[x+1]:
            tup = (number[x],x)
            dups.append(tup)

            
                   
            return True
    return False

def has_not_dec(number):
    for x in range(0,5):
        if number[x] > number[x+1]:
            return False
            
    return True

min = 111111
max = 111411

count = 0
for num in range(min,max):
    res = [int(x) for x in str(num)] 
    
    one = has_dup(res)
    two = has_not_dec(res)

    if one == True & two == True:
        count+=1
print(count)
def has_dup(number):
    for x in range(0,5):
        if number[x] == number[x+1]:
            return True
    return False

def has_not_dec(number):
    for x in range(0,5):
        if number[x] > number[x+1]:
            return False
            
    return True

min = 109165
max = 576723

count = 0
for num in range(min,max):
    res = [int(x) for x in str(num)] 
    
    one = has_dup(res)
    two = has_not_dec(res)

    if one == True & two == True:
        count+=1
print(count)
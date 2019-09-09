Z = input("Enter the product : ")
def cartvalue(Z):
    count_A = count_B = count_C = count_D = 0
    sum_A = sum_B = sum_C = sum_D = special_A = special_B = 0
    for x in Z:
        if x =='A': count_A+=1
        if x =='B': count_B+=1
        if x =='C': count_C+=1; sum_C = 20*count_C
        if x =='D': count_D+=1; sum_D = 15*count_D 
    if count_A>0: acount = count_A%3; setacount = count_A//3; sum_A = 50*acount; special_A = 130*setacount
    if count_B>0: bcount = count_B%2; setbcount = count_B//2; sum_B = 30*bcount; special_B = 45*setbcount        
    total_cartval = sum_A + sum_B + sum_C + sum_D + special_A + special_B
    return total_cartval
print("Total cart value :", cartvalue(Z))
sum=0
for i in range(1111,10000,1):
    if i%1234==0:
        continue
    elif sum+i >=100000:
        break
    else:
        sum +=i
print("=")
print(sum)

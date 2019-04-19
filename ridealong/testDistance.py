test=[10,30,50,60,70,80]
i=0
while i < len(test):
    if(test[i]%3==0):
        del test[i]
    else:
        print(test[i])
        i+=1



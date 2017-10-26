n = int(input('input a number:'))
k = 1
while n >= k:
    for i in range(1,n+1):
        while_ans = i*k
        print('%d*%d=%d'%(k,i,while_ans))
        #print(str(k)+'*'+str(i) + '=' + str(while_ans))
    k=k+1
    
for i in range(1,n+1):
    for j in range(1,n+1):
        for_ans = i * j
        print('%(#1)d*%(#2)d=%(#3)d'%{'#1':i,'#2':j,'#3':for_ans})
        #print(str(i)+'*'+str(j) + '=' + str(for_ans))

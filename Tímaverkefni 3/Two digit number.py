AB=1 
CAB=AB*AB 
last2=int(str(CAB)[-2:]) 
while len(str(CAB))!=3:
     AB+=1 
     CAB=AB*AB 
while AB!=last2:
     AB+=1 
     CAB=AB*AB 
     last2=int(str(CAB)[-2:])

print(AB)

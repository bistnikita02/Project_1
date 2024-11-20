import math
from users.models import Skill 

def cosine_similarity(user,vacancy):
    sumXX,sumYY,sumXY=0,0,0
    #i=0
    for X,Y in zip(user,vacancy):   
        sumXX += X**2
        sumYY += Y**2
        sumXY+=X*Y
           # i=i+1

    square_root = math.sqrt(sumXX*sumYY) 
    if square_root == 0:
        return 0  
    return(sumXY/math.sqrt(sumXX*sumYY))

 
skills = list(Skill.objects.values_list('name', flat=True))

def vectorize(x = []):
    matrix=[]
    for skill in skills:
        if skill in x:
            matrix.append(1)
        else:
            matrix.append(0)
            
    return matrix

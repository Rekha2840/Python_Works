# Module name = Decor

# This module conatins repetetive codes which
# are used for non calculation purposes
#FOR REPETATIVE DECORS


def hr(size=16, gap=5, shape="="):
    for x in range(1,size):    
        print(str(shape),end="")
        if x% gap is 0:
            print(" ",end=" ")


def sp(x=1):
    for c in range(0,x):
        print("")

def sp1():
    print('')
    print('')
     

#EDITED RESERVED WORDS
def cout(*x):        #cout == print
    args= len(x)
    for s in range(0,args):
        print(x[s], end=" ")
    print("")        
 


#PYRAMID AND OTHER PATTERNS
#Simple pyramid
def prymd(line=3,shape="*"):        
    try:        
        shape= str(shape)
        pttrn=[];
        for c in range(1,line+1):
            pttrn.append(shape*c)    
        for I in range(0,line):
            print( pttrn[I] ) 
    except TypeError:
        print("{ Argument 1 of prymd func takes lines and argument 2 takes shape  }")       
        
#Reverse version       
def rprymd(line=3,shape="*"):        
    try:        
        shape= str(shape)
        pttrn=[];
        for c in range(1,line+1):
            pttrn.append(shape*c)    
        for I in range(0,line)[::-1]:
            print( pttrn[I] ) 
    except TypeError:
        print("{ Argument 1 of rprymd func takes lines and argument 2 takes shape  }")       
              

#Prints a Factorial Pyramid
from matrixpy import factorial
def factr_prymd(num):
    arr = []; ctr = '';
    for x in range(1,num+1):
        for y in range(x):
            ctr += str(y+1)
            if y == x - 1:
                if x != 1:
                    ctr+= "  = {0}".format(str(factorial(x)))
            else:
                ctr += "x";
        arr.append(ctr)
        ctr = '' 
    for arg in arr:
        print(arg)




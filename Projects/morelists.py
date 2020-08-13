#Functions only for list manupulation

#Copies data from list to other list and deletes original
def cutlist(froms, to):    
    try:
        for x in range(len(froms)):
            to.append(froms[x]) 
        for x in range(len(to)):    
            froms.remove(froms[0])
        return to;
    except IndexError:
        IndexException= "{  IndexError: argument 2 values should be left null   }"
        return IndexException


#Copies data from a list to another without deleting original
def copylist(froms, to):        
        for x in range(len(froms)):
            to.append(froms[x])         
        return to;
    
     
#Randlist function for creating a random list of integers
def randlist(strt, end, args=5):
    from random import randint
    try:
        arr= []; 
        while True:
            num= randint(strt, end)
            arr.append(num);
            if len(arr) is args:
                break;
        return arr 
    except ValueError:
        ValueException= "{  ValueError: rangrand function argument2 should be larger than argument1  }"         
        return ValueException
        
 
#random.choice edited, allows multiple choices 
def randchoices(arr,num=1):
    from random import randint
    times= len(arr); newarr= [];
    for x in range(num):
        randnum= randint(0,times-1);
        newarr.append(arr[randnum])
    return newarr;
  
    
#Loop function for creating instance loops as list
def looper(x, y,z=1):    
    arr=[];
    if x<y:
        z=z
    else:   
        if z<0:
            z=z
        else:
            z=-z 
    for args in range(x, y, z):
        arr.append(args)        
    return arr

#Index function 2ndV , returns multiple values if multiple nums true
def find(arr,num):
    arr2 =[]; 
    for c in range(len(arr)):
        if arr[c] == num :
            arr2.append(c)           
    if len(arr2) is 1:        
        return arr2[0];
    elif len(arr2)> 1:
        return arr2
    else: return None;    


def remove(arr,index):
    lst= []
    copylist(arr,lst)
    if index == len(lst) - 1 :
        lst.remove(lst[index])
    else:
        lst= []
        for arg in range(len(arr)):
            if arg == index:
                continue
            lst.append(arr[arg])
    return lst


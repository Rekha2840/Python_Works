# This module is for custom made functions for specific mathematical uses
#and dictorary functions

import random

#Python Print function  as cout
def cout(*x):
  args=len(x)
  for s in range(0,args):
    print(x[s], end=" ")
  print("")


      
#exp function that calculates a number power(replacement for **)
def exp(x,y):
    try:
        arr= [];
        for count in range(0, y):
            arr.append(x)        
        total= 1;  
        for rsl in range(0,len(arr)):
            total*=arr[rsl]
        return total 
    except TypeError:          
        exception= "{ Function 'exp' arguments take only integers }"
        return exception
 
 
#dict_sort function for sorting data in dictionaries
def dict_sort(dict_data, times='all'):   
    if times is "all": times= len(dict_data)
    from operator import itemgetter
    count= 0;     arr=[];     arr1=[];  arr2=[];     
    dat= sorted(zip(dict_data[0].keys()));
    
    if len(dat) is 2:
        for x in sorted(dict_data, key=itemgetter(dat[0][0], dat[1][0])):        
            count+= 1;
            arr.append(x[dat[0][0]])            
            arr1.append(x[dat[1][0]])    #Loops iterate dict
            if count== times: break; 
        final= list(zip(arr, arr1));  check= len(final);
    if len(dat) is 3:
        for x in sorted(dict_data, key=itemgetter(dat[0][0], dat[1][0],dat[2][0])):        
            count+= 1;
            arr.append(x[dat[0][0]])            
            arr1.append(x[dat[1][0]])    #Loops iterate dict
            arr2.append(x[dat[2][0]])
            if count== times: break; 
        final= list(zip(arr, arr1,arr2));  check= len(final); 
        
    TypeException= "TypeError: in dict_sort function, argument 1 has "+str(check)+" keys, Entered: "+str(times);      
    try:    
        test= dat[3][0]
    except IndexError:        # If len(keys) not 2
        IndexException= "IndexError" 
    finally:
        if len(dat) > 3:  
            IndexException= "  {IndexError: Function 'dict_sort' takes only 2 keys at maximum}"
            return IndexException  
        else:        
            try:
                if times > check:  # if len(keys)== 2
                    return TypeException
            except TypeError:
                ValueException= "  {Value error:argument 2 takes only integer}"
                return ValueException         
            else: return final

          
#Ratio prints a percent of a number                             
def ratio(percent,num):
    return ((num*percent)/100)

#Reverse of the ratio function, gets the percent num1 takes on num2
def get_ratio(small, big):
    percent = (small * 100) / big
    return percent


#Returns factors of a number 
def factor(num, strt=1,end='all'):
    nums=[]; no= num;
    if end is 'all': end= num;
    for a in range(strt,end):
        nums.append(a)     
    chance = list(filter(lambda x: num%x ==0,nums))      
    for b in range(0,len(chance)):
        factors= chance
    return factors    


#Checks how many times a number repated in array
def check(num, arr):    
    filtered_arr= list(filter(lambda x: x==num, arr))
    return len(filtered_arr)


#Rounds digits after a float point
def roundto(num, dgts):
    try:
        strnum= str(num); pt= strnum.index(".")
        bfr= strnum[0:pt]; afr= strnum[pt+1:pt+dgts+1];
        newnum= bfr+"."+afr; newnum1= float(newnum);     
        return newnum1
    except ValueError:
        inp_type= str(type(num))
        Indexexception= "Argument 1 should be a float type not "+inp_type[7:-1]
        return Indexexception


#Returns a bool value of random chance (for random chances)
def rand_chance(num,out_of=100):
    num= abs(num)
    rand_num= random.randrange(num,out_of)
    print(rand_num)
    if rand_num <= num :
        return True
    return False



#Returns the factorial number (ex: 5! = 1x2x3x4x5 )
def factorial(num):
    value = 1
    for x in range(1,num+1):
        value *= x
    return value









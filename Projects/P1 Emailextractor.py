#Language ==python3
import zdecor
import re

def main():
    zdecor.sp1()
    accs=input("Enter some words along some E-mail ID\n>> ")
    pttrn=r"(([\w\-]+|\w\d\-]+)@([\w]+)((.[\w]+)|(.([\w])+([\.\w])+)))";
    mtch=re.findall(pttrn, accs)    
      
    len_mtch=len(mtch) 
    zdecor.sp1() 
    if mtch!=None:                	        	        	                
        for x in range(0,len_mtch) :
            print(mtch[x][0])           
   
    if len_mtch==0:
        print("Sorry, but no E-mail IDs were found")   


if __name__=='__main__':
    main()    
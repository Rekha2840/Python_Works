import time
m31=[1,3,5,7,8,10,12]; m30= [4,6,9,11]; 
  
def fmd(d, m, y): #First month days
    global m30,m31;
    dom= 0; 
    if m in m31: dom= 31;
    elif m in m30: dom= 30;
    else: 
        if y%4==0: dom= 29;
        else: dom= 28;    
    return dom- d;  
def fyd(d,m,y): #First year days
    global m30,m31;  doy=0;
    for month in range(m+1,13):
        if month in m31: doy+=31;
        elif month in m30: doy+=30
        else: 
            if y%4==0: doy+= 29;
            else: doy+= 28;    
    return doy + fmd(d, m, y )


localtime= time.localtime(time.time())
docm= localtime[2] #Todays' date (Days passed since date 1 of month)
def cyd(m, y): #Days passed in current year since jan1
    global localtime,m30,m31,docm; arr=[]; docy= 0;
    for months in range(1,m)[::-1]: arr.append(months)
    for month in arr:
        if month in m31: docy+=31;
        elif month in m30: docy+=30
        else: 
            if y%4==0: docy+= 29;
            else: docy+= 28;   
    return docy + docm


while True:
        try:                      
            dob= int(input("Enter Date of Birth:  "));
            mob= int(input("Enter Month of Birth:  "))
            yob= int(input("Enter Year of Birth:  "));
        except ValueError:
            print("\n Enter only Integeral values! ", "\n")
        finally:
            break;

def check_errors(): #Errors which cant be done thro excptions
    error= None
    global dob, mob, yob, m31, m30 ,localtime;
    mnt=["January","February","March","April","May","June","July",
    "August","September","October","November","December" ]    
    if dob<1 or dob>31: error= "No month has a day "+str(dob);       
    try:        
        if mob in m30 and dob>30:error= mnt[mob-1]+" does not have more than 30 days ";               
        if mob == 2 and yob% 4==0 and dob>29:error= "February does not have more than 29 days in a leap year"
        elif mob == 2 and yob%4!=0 and dob> 28:error="February does not have more than 28 days on a normal year"
    except IndexError:    
        error= "Unexpected input Error, try again" 
    if mob<1 or mob>31: error= "No year has a month "+str(mob);     
    if yob>localtime[0]:error= "Year cannot exceed "+str(localtime[0])
    elif yob== localtime[0]:
        cutm= "Inputs cannot exceed ("+str(localtime[0])+"/"+str(localtime[1])+"/"+str(localtime[2])+")"
      #new var cutm since errors are similar below
        if mob>localtime[1]: error= cutm;
        elif mob==localtime[1]:
            if dob>localtime[2]: error= cutm;                
    if error!=None:
        return "\n"+str(error)
    return error
    

def main():
    global dob, mob, yob, localtime;
    days= 0; 
    for year in range(yob+1,localtime[0]):
        if year% 4==0:    
            days+=366
        else:
            days+= 365    
    if yob == localtime[0]:
        if localtime[0]% 4==0: days-=366        
        elif localtime[0]%4!=0: days-=365                                      
    day_curr_year= cyd(localtime[1],localtime[0])
    day_year1= fyd(dob, mob, yob)
    totaldays= day_year1 + day_curr_year + days       
    if totaldays == 0:
       print("\n CONGRATS! , You're born today!")
    else:   
        print("\n","\n Days passed since your Birth: ",totaldays,end="")              
        if totaldays > 1:
            print("Days")
        elif totaldays==1: 
            print("Day")    
        
   
if __name__=='__main__':
    if check_errors()==None:
        main()
    else:    
        print(check_errors())
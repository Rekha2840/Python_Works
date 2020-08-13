#Language== Python3.6
#Red Decks Python game
import re
from zdecor import cout, sp, hr
from morelists import randchoices, randlist
from random import randint, choice
from filefunc import file
import time
#Money functions
arr1=[];
def load_game(x= arr1):
    global arr1
    f1= file("dats/scores.txt")
    for c in range(2):
        arr1.append(int(f1.get_line(c+1)))
    f1.close();
load_game()            
bucks= (arr1[0]); hs= arr1[1]; sp(2);
cash= bucks; hisc= hs;  

# Shows the stats of the player
def menu():
    print(" Money: ",int(cash),"$","\t","\t","\t","\t   HighScore: ",int(hisc),"$ \n");hr(40,4,"▪")
    
    	
#Cards and players  
coms1= ["Bucky","DonkeyKong","Mahbuss","Jack","Marley","DonJuon","Rook","Bartelomeo","BigFish7","George","Sertfgh","IisShitName"]
coms2=["Gusion","FireFistAce","Bruno","CrazyDave","Manhog","Carrots","Roger","Tom","DonQasd","Machete","LukeSkywalker","Steve","Riku"]
coms= coms1+ coms2; a= randint(2,10);b = randint(2,10); c= randint(1,10)
sh=  a, a, a,; sd= a, a+1, a+2;
sn= a, b,c; sc= a, a, c; 
cards=[str(sc),str(sn),str(sn),str(sd),"King, queen and jack",str(sh),"ThreeofAce","ThreeKings","ThreeQueen","ThreeJacks"]
pwr= [2,1,2,4,6,5,8,7,7,7]

        
      ########## ########## ########## ########## ##########  
#First Setup      
menu(); sp(3);
def showrules():
    print("RULES");hr(6,6,"-");sp(2);    print("  Each level, there will be several rounds, according to number of players, the players will get three random cards. ")
    print("  The highest score on cars will reamin and lowest will dropout."); sp();
    print("You can choose to leave match after 2 rounds of the game, if you are the last winner, you get bonus $$$$")
showrules(); sp(4);	   
print("DIFFICUILTY"); hr(14,7,"-");sp(2);
cout("Level 1: Slow, more players, less risk, For playin safe")
cout("Level 2: Moderate, for experienced players")
cout("Level 3: Extreme, are you ready for the challenge? ");sp(2);
while True:
    pnum= int(input("CHOOSE LEVEL NO >> ")) 
    if pnum<=3:
        if pnum== 1: noplyrs= 6
        if pnum== 2: noplyrs= randint(4,5)
        if pnum== 3: noplyrs= 3
        break;
    if pnum>=4:
        print("Choose level1, level2 or level 3".upper(),"\n"); hr(); sp(6);
sp(3);         
players= ["you"]+ randchoices(coms,noplyrs);
print("The players are",end="  ")
for x in range(0,len(players)):
    print(players[x], end=", ")    
    if len(players)- x ==2:
        break               
print(" and ",players[-1],end=" "); sp(3);    
 
#Game background inputs and datas
rsl= choice(list(zip(cards, pwr)))
comgot= []; compts=[];  comcards=[];  #players pts and cards
for x in range(0,len(players)):
    cards2=[str(sc),str(sn),str(sn),str(sd),"King, queen and jack",str(sh),"ThreeofAce","ThreeKings","ThreeQueen","ThreeJacks"]
    pwr2= [2,1,2,4,6,5,8,7,7,7]
    rsl2= choice(list(zip(cards2, pwr2)))    
    comgot.append(rsl2)  
for x in range(0,len(comgot)):    
    compts.append(comgot[x][1])    
    comcards.append(comgot[x][0])   
allpts= sorted(zip(compts, players))
allcards= list(zip(compts, players))
allgot= list(zip(comcards, players))
cout("Start? ")
start= str(input("(y/n) :   "))

#Game front output
if start =="y" or start=="yes" or start=="Y":
    count= 0; lv= 1; profit=0; loss=0; profit2= 0;
    if cash< 0: cash=0;
    def print_total():
        sp(4)
        print("PROFIT: ",int(profit2),"$ \t","\t","\t","LOSS: ",int(loss),"$")
        sp(3)
        print("MONEY: ",int(cash) ,"$ \t","\t","\t","HISCORE: ",int(hisc),"$")
    while True:
        time.sleep(0.5)       
        sp(80)
    
    
        if len(players) is 1:               
            sp(6); print("YOU BEAT EM' ALL"); sp(3);             
            print_total()   
            break
        menu(); sp(4);    
        print("\t","\t","\t","\t ROUND ",lv) #Playrs left
        sp(3); print("  Players ",end= " :  ") 
        sp();
        for x in range(len(players)):    
            print("       ",x+1,". ", players[x])    
      
        if pnum== 1: minb=  10;             #MINIMUM BETS
        if pnum== 2: minb=  40;
        if pnum== 3: minb=  75;                
        sp(10); print("Minimum bet: ",minb); sp();
        while True:
            bet= int(input("Please make a bet: "))
            
            if bet>= minb and bet<= cash:
                print(" YOUR BET: ",bet,"$") 
                cash-= bet
                break                
            if bet< minb: print("Minimum bet reqd is ",minb,"\n")                                             
            if cash < bet and lv <4:
                print("Not Enough MONEY")                
                ask= str(input("Bet again"))
                sp(3)
            if cash < bet and lv > 3:
                print("Not Enough money, leave or play?")
                ask= str(input("y-leave , n-play"))
                sp(3)
                if ask !="y":
                    break;                   
                    
                                   
        bets= randlist(minb*2, minb*10,len(players))         
        turns= bets[1::]; plyr= players[1::]                  
        for x in range(1,len(players)):
            time.sleep(0.6)
            print(players[x],"betted for",bets[x],"$")
        sp(3)  
          
                
        
        if lv>= 3:            #retreat after round 3
            sp(5);
            print("Proceed to next round? (You can leave now)   ")            
            next= str(input("(y/n): "))    
            if next == "n" or next == "no" or next== "nah":   
                cash+= bet 
                print_total()
                break;  sp(5);                
                
                
        for x in range(len(players)):
            time.sleep(0.7)
            print(allgot[x][1]," got ", allgot[x][0] )
            print("  POWER: ", allcards[x][0]," . ")
            sp(3) 
                
        if allpts[0][1] != "you":      #if p1 not lost
            print(allpts[0][1]," has been eliminated.")                                
            loc= (plyr.index(str(allpts[0][1]))) #Who lost's $$
            profit+= (bets[loc]/len(players)-1)+bet*lv #Profit divided by players left
            cash+= profit; profit2+= profit
            if cash >= hisc: hisc= cash
            else: hisc= cash
            print("You get ",profit,"$")
            profit= 0
        if allpts[0][1] == "you":      #if p1 lost
            print(allpts[0][1]," have been eliminated.")            
            if lv<4:
                loss+= bet/lv
                cash-= loss
            print_total()    
            break
        players.remove(str(allpts[0][1]))
        allpts.remove(allpts[0])
                
        if lv<4:  #Pause
            sp()
            next= str(input("Press enter to continue"))
                                         
        count+=1; lv+=1;      
        
      ########## ########## ########## ########## ##########       
#saving game
arrt=[int(cash), int(hisc)];    #rounding up
def save_game():
    global arrt
    f1= file("dats/scores.txt")
    for c in range(len(arrt)):
       f1.insert(c+1,arrt[c])
    f1.close();
save_game()
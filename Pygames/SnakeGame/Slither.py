import pygame as pyg
from filefunc import file
import random
pyg.init()

#colors
black= (0,0,0)
white= (255,255,255)
red=(255,0,0)
green= (0,170,0)

display_width= 1200
display_height= 600

gameDisplay= pyg.display.set_mode((display_width,display_height))
pyg.display.set_caption("Slither")
gameStart= False

clock= pyg.time.Clock()
FPS= 15

snakehead= pyg.image.load("snakehead.png")
apple= pyg.image.load("apple.png")


def load_score():
    f1 = file("hscore.txt")
    try:
        hscore= f1.get_line(1)
        return hscore
    finally:
        f1.close()
#High Score of the player
hscore= load_score()

def write(score):
    f1= file("hscore.txt")
    f1.insert(1,score)
    f1.close()


def any_match(ls1,ls2):
    for eachItem in ls1:
        for eachItem2 in ls2:
            if eachItem == eachItem2:
              return True
    return False


def collision(obj1_s,obj1_e,obj2_s,obj2_e):
    ob1_x= list(range(int(obj1_s[0]),int(obj1_e[0]+1)))
    ob1_y = list(range(int(obj1_s[1]), int(obj1_e[1] + 1)))
    ob2_x = list(range(int(obj2_s[0]), int(obj2_e[0] + 1)))
    ob2_y = list(range(int(obj2_s[1]), int(obj2_e[1] + 1)))
    #X-crossover + Y-crossover == True
    if any_match(ob1_x,ob2_x) and any_match(ob1_y,ob2_y):
        return True
    return False

def ratio(percent,num):
    return int((num*percent)/100)


def message_to_screen(msg,color,size,pos_x=display_width/2,pos_y=display_height/2,fontStyle= "comicsansms"):
    font= pyg.font.SysFont(fontStyle,size)
    screen_text= font.render(msg,True,color)
    gameDisplay.blit(screen_text,[int(pos_x),int(pos_y)])


def round_to(number,digit):
    return round(number/float(digit)) * float(digit)

def pause():
    paused= True
    while paused:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                quit()
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_p:
                    paused= False
        message_to_screen("Paused",black,90,ratio(35,display_width),ratio(25,display_height))
        message_to_screen("Click p again to continue", black,40, ratio(30, display_width), ratio(51, display_height))
        pyg.display.update()
        clock.tick(5)

def snake(block_size,snakelist,pos_X,pos_Y,dir):
    if dir == 'right':
        head= pyg.transform.rotate(snakehead,270)
    elif dir == 'left':
        head= pyg.transform.rotate(snakehead,90)
    elif dir== 'down':
        head= pyg.transform.rotate(snakehead,180)
    else:
        head= snakehead

    for XnY in snakelist:
        pyg.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])
        gameDisplay.blit(head, [pos_X, pos_Y])


def gameLoop():
    global gameStart, hscore
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 10
    lead_y_change = 0

    block_size= 20
    appleThickness= 30
    speed= 15

    score= 0
    snakelist = []
    snakeLength= 3
    direction= 'right'

    appleX= round_to(random.randrange(0,display_width-block_size),10)
    appleY= round_to(random.randrange(0,display_height-block_size),10)

    gameExit = False
    gameOver= False
    level= 1

    #Message before game Starts
    while gameStart == False:
        gameDisplay.fill(white)
        message_to_screen("Welcome To Slither!",green,70,ratio(20,display_width),ratio(10,display_height))
        message_to_screen("Use W,S,A,D keys to move Up, Down, Right and left. ",black,22,ratio(15,display_width),ratio(40,display_height))
        message_to_screen("Eat the Apples to increase score and set your own records!", black, 22, ratio(15, display_width),ratio(45, display_height))
        message_to_screen("You will lose if you go off the ground or crash onto yourself!", black, 22, ratio(15, display_width),ratio(50, display_height))
        message_to_screen("Its not that easy! The snake will go faster as level increases!", black, 22, ratio(15, display_width),ratio(56, display_height))
        message_to_screen("Press s to start game or q to quit", green, 50,ratio(17,display_width),ratio(72,display_height))
        pyg.display.update()
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                gameExit = True
                gameStart= True
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_q:
                    gameExit = True
                    gameStart= True
                if event.key == pyg.K_s:
                    gameStart = True
                    gameLoop()

    while not gameExit:
        #Message after Lost
        while gameOver == True:
            if int(score) > int(hscore):
                hscore= score
                message_to_screen("New Length Record!",black,50,ratio(31,display_width),ratio(21,display_height))
                message_to_screen(" NEW HIGH SCORE: {0}".format(str(hscore)),green,55, ratio(26, display_width),ratio(37, display_height))
            elif int(score) < int(hscore):
                message_to_screen('GAME OVER!',red,65,ratio(32,display_width),ratio(30,display_height))
                message_to_screen("HIGH SCORE: {0}".format(str(hscore)),black,45,ratio(31,display_width),ratio(2,display_height))
            write(hscore)
            message_to_screen("Press r to Retry or q to Quit", black, 40, ratio(31,display_width),ratio(60,display_height))
            pyg.display.update()
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    gameExit = True
                    gameOver= False
                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pyg.K_r:
                        gameLoop()

        #Event loop
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                gameExit= True
            if event.type== pyg.KEYDOWN:
                if event.key == pyg.K_a:  # Left
                    if lead_x_change == 10: direction= "right"; lead_x_change= lead_x_change
                    else: direction= "left"; lead_x_change= -10
                    lead_y_change = 0
                elif event.key == pyg.K_d:  # Right
                    if lead_x_change == -10: direction="left"; lead_x_change= lead_x_change
                    else: direction= "right"; lead_x_change= 10
                    lead_y_change = 0
                elif event.key == pyg.K_w:  # UP
                    if lead_y_change== 10: direction= "down"; lead_y_change= lead_y_change;
                    else: direction= "up"; lead_y_change= -10
                    lead_x_change= 0
                elif event.key == pyg.K_s:  # Down
                    if lead_y_change== -10: direction= "up"; lead_y_change= lead_y_change;
                    else: lead_y_change= 10; direction= "down"
                    lead_x_change = 0
                elif event.key == pyg.K_p:
                    pause()

        #Game over
        if lead_x >= display_width-display_width/100 or lead_x < 0 or lead_y >= display_height-display_height/100 or lead_y < 0:
            gameOver= True

        lead_x += lead_x_change
        lead_y += lead_y_change

        #Snake ate apple
        ob1_s = (lead_x, lead_y)
        ob1_e = (lead_x + block_size, lead_y + block_size)
        ob2_s = (appleX, appleY)
        ob2_e= (appleX+appleThickness,appleY+appleThickness)
        if collision(ob1_s,ob1_e,ob2_s,ob2_e) == True: #Collsiion eas detected
            appleX = random.randrange(0, display_width - appleThickness)
            appleY = random.randrange(0, display_height - appleThickness)
            snakeLength += 1
            score += 10
            if score % 100 == 0:
                level += 1
                speed+=5

        #Renderer_display
        gameDisplay.fill(white)
        #pyg.draw.rect(gameDisplay,red,[appleX,appleY,appleThickness,appleThickness]) #Apple
        gameDisplay.blit(apple,[appleX,appleY]) #Apple
        message_to_screen("Level: {0}".format(str(level)),black,32,5,2,fontStyle="trebuchetms") #Lvl
        message_to_screen("Score: {0}".format(str(score)),black,32,display_width-display_width/7,2,fontStyle="trebuchetms") #Score
        #Snake functions
        snakehead= []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        snake(block_size,snakelist,lead_x,lead_y,direction)

        pyg.display.update()
        clock.tick(speed)

        #Controlls snake length
        if len(snakelist) > snakeLength:
            del snakelist[0]
        #Gameover if snake hits itself
        for eachSnakeParts in snakelist[:-1]:
            if snakehead == eachSnakeParts:
                gameOver= True

    pyg.quit()
    quit()
gameLoop()
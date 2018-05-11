#to create a dataset out of colour pallete 
#IT helps in creating a test,training dataset which is used for testing and trainning purpose.
# 1 = BLACK , 0 = WHITE

import pygame
import random as r
import csv


pygame.init()
exit_var = False
'''Counter - No of readings'''
count = 0


green = (0,255,0)
white = [255,255,255]
black  = [0,0,0]
colour_1 = [255,255,255]


font = pygame.font.Font("freesansbold.ttf",25)
head_font = pygame.font.SysFont("comicsansms", 25)


def text_black(msg, font):
    screen_text = font.render(msg,True,black)
    return screen_text,screen_text.get_rect()

def text_white(msg, font):
    screen_text = font.render(msg,True,white)
    return screen_text,screen_text.get_rect()


headSurf = head_font.render("Choose the Text which suits the most for the background", True, (0, 0, 0))


def colour_update1():
    a = r.randrange(0,255,1)
    b = r.randrange(0,255,1)
    c = r.randrange(0,255,1)
    colour_1[0] = a
    colour_1[1] = b
    colour_1[2] = c
    pass




data_disp = pygame.display.set_mode((800,600))
pygame.display.set_caption('Data set')

data_disp.fill(white)

with open('test1.csv','w',newline='') as f:
    thewriter = csv.writer(f)

    while not exit_var: 
        for event in pygame.event.get():
    
            if event.type == pygame.QUIT:
                exit_var = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if (mx > 100 and mx < 300 ) and (my > 300 and my < 400):
                    c = list(colour_1)
                    print(colour_1)
                    c.insert(0,1)
                    #print(c)
                    thewriter.writerow(c)
                    colour_update1()
                    count +=1
                    print(count)
                        
                if (mx > 400 and mx < 600 ) and (my > 300 and my < 400):
                    d = list(colour_1)
                    d.insert(0,0)
                    #print(d)
                    thewriter.writerow(d)
                    colour_update1()
                    count +=1
                    print(count)
                        
                if (mx>400 and mx<420) and (my>500 and my<520):
                    colour_update1()
                        
                
                
        textSurf1 , text_objectRect1 = text_black("TEXT 1", font)
        textSurf2 , text_objectRect2 = text_white("TEXT 2", font)
            
        text_c1 = ((100+50),(300+50))
        text_c2 = ((400+50),(300+50))
        head_c  = ((50),(200))
                
        data_disp.fill(colour_1,rect = [100,300,200,100])
        data_disp.fill(colour_1,rect = [400,300,200,100])
        data_disp.fill(green, rect = [400,500,20,20])
        
        #text feild 
        data_disp.blit(textSurf1,text_c1)
        data_disp.blit(textSurf2,text_c2)
        data_disp.blit(headSurf,head_c)        
                
        pygame.display.update()


pygame.quit()
quit()
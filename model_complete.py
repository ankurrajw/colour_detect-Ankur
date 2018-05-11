# -*- coding: utf-8 -*-
"""
Created on Fri May 11 18:42:22 2018

@author: Ankur Raj
"""
#   Testing the neural Network, and display the result in real time 
# 1 = BLACK , 0 = WHITE
#basic needed packages
import pygame
import random as r
import numpy as np
from neural import neural_net

#BASIC Neural Network Structure
input_node = 3
hidden_node = 5
output_node = 2
'''learning rate'''
learning_rate = 0.2

'''counter 1 - Number of time neural network is excequted'''
lcount = 1
'''counter 2 - accuracy chcek'''
a=0
'''accuracy limit'''
limit = 0.93

#Check the accuracy limit with the current value of accuracy, which changes continuously

while a != limit:
    '''class object/instance'''
    n = neural_net(input_node,hidden_node,output_node,learning_rate)
# opennning the files of trainning and testing
    score = []#score card to check accurary value for test dataset
    f = open('data1.csv','r')
    f_list = f.readlines()
    f.close()
    
    t = open('test.csv','r')
    t_list = t.readlines()
    t.close()
    epoch = 6# epoch value
    #Trainning:-
    for i in range(epoch):

        for record in f_list:
            all_val = record.split(',')
            inputs = (np.asfarray(all_val[1:])/255.0*0.99)+0.01
            targets = np.zeros(output_node) +0.01
                
            targets[int(all_val[0])] = 0.99
            #training of the model for a spceific value of weights
            n.training(inputs , targets)
            pass
    #Testing:-
    for record in t_list:
        all_val = record.split(',')
        correct_label = int(all_val[0])
        inputs = (np.asfarray(all_val[1:])/255.0*0.99)+0.01
        outputs = n.query(inputs)
        label = np.argmax(outputs)
        if label == correct_label:
            score.append(1)
        else:
            score.append(0)
            pass
        pass
    print(score)
    n_val = np.asfarray(score)
#accuracy, num
    num = n_val.sum()/n_val.size
    print('performence - ',num)
    a = round(num,2)
    print(a)
    print('Test Case - ',lcount)
    lcount+=1#Number of times the neural network value changes
    

"""Finaly the model of neural net which has the higher value of accuracy is chosen
    and is fed to the pygame interface."""
    
#Pygame Interface
pygame.init()

a = 0 

exit_var = False
'''COUNTER -3'''
count = 0

#INITIAL COLOURS
green = (0,255,0)
white = [255,255,255]
black  = [0,0,0]
colour_1 = [255,255,255]

#Font styles
font = pygame.font.Font("freesansbold.ttf",25)
head_font = pygame.font.SysFont("comicsansms", 25)

#Black Text
def text_black(msg, font):
    screen_text = font.render(msg,True,black)
    return screen_text,screen_text.get_rect()

#White Text
def text_white(msg, font):
    screen_text = font.render(msg,True,white)
    return screen_text,screen_text.get_rect()

#Changes the colour value when called.
def colour_update1():
    a = r.randrange(0,255,1)
    b = r.randrange(0,255,1)
    c = r.randrange(0,255,1)
    colour_1[0] = a
    colour_1[1] = b
    colour_1[2] = c
    pass

#Content Text
headSurf = head_font.render("Choose the Text which suits the most for the background", True, (0, 0, 0))

#Background Display size
data_disp = pygame.display.set_mode((800,600))
#Title
pygame.display.set_caption('Data set')
'''Fills the Display with white colour'''
data_disp.fill(white)

'''Game loop
    0 :- White
    1 :- Black
'''
while not exit_var:
    '''Test the given colour value with our neural netowork model
    and then choose weather black or white text suits the most.'''
    
    colconv = (np.asfarray([colour_1])/255.0*0.99) + 0.01
    result = n.query(colconv)
    b = np.argmax(result)#which text colour suits the most.
    if b == 0:
        colour_3 = white #Updates the value of colour
        colour_4 = black
    else:
        colour_3 = black
        colour_4 = white
        pass

#Event game loop
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit_var = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx,my = pygame.mouse.get_pos()
            if (mx > 100 and mx < 300 ) and (my > 300 and my < 400):
                colour_update1()
                    
            if (mx > 400 and mx < 600 ) and (my > 300 and my < 400):
                d = list(colour_1)
                colour_update1()
            
            #Updating background colour manually
            if (mx>400 and mx<420) and (my>500 and my<520):
                colour_update1()
                    
            
    '''Text Object B/W'''
    textSurf1 , text_objectRect1 = text_black("TEXT 1", font)
    textSurf2 , text_objectRect2 = text_white("TEXT 2", font)
    
    '''Text Location'''
    text_c1 = ((100+50),(300+50))
    text_c2 = ((400+50),(300+50))
    head_c  = ((50),(200))
    
    '''Colour of Text Box, Update box, Neural box'''
    data_disp.fill(colour_1,rect = [100,300,200,100])
    data_disp.fill(colour_1,rect = [400,300,200,100])
    data_disp.fill(green, rect = [400,500,20,20])
    data_disp.fill(colour_3,rect = [150,250,10,10])
    data_disp.fill(colour_4, rect =[450,250,10,10])
    
    '''Text Box - Text'''
    data_disp.blit(textSurf1,text_c1)
    data_disp.blit(textSurf2,text_c2)
    data_disp.blit(headSurf,head_c)        
    
    '''Update'''
    pygame.display.update()

'''Quit Statement'''
pygame.quit()
quit()
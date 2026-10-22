import pygame
import time
from random import*



pygame.init()
temp=0
score =0
snake_body=[100,50]
snake_position = [[100, 50],[90, 50],[80, 50],[70, 50]]
clock = pygame.time.Clock()
window = pygame.display.set_mode((1080,900))
run = True
direction = 'RIGHT'
change_to = direction
fruitpos=[randint(1,108)*10,randint(1,90)*10,10,10]
ruitpos=[randint(1,108)*10,randint(1,90)*10,10,10]

font = pygame.font.SysFont('times new roman',30)
fonta = pygame.font.SysFont('concrete roman',100)

def die():
    window.blit(died,(100,400))
    pygame.display.update()
    time.sleep(2)
    quit()


while run:
    
    text = font.render("Score:"+str(score),True,(0,255,255),0)
    clock.tick(20)
    snake_temp=snake_body[:]


   



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                change_to = 'UP'
            if event.key == pygame.K_s:
                change_to = 'DOWN'
            if event.key == pygame.K_a:
                change_to = 'LEFT'
            if event.key == pygame.K_d:
                change_to = 'RIGHT'
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if direction == 'UP':
        snake_temp[1] -= 10
        snake_body[1] -= 10
    if direction == 'DOWN':
        snake_temp[1] += 10
        snake_body[1] += 10
    if direction == 'LEFT':
        snake_temp[0] -= 10
        snake_body[0] -= 10
    if direction == 'RIGHT':
        snake_temp[0] += 10
        snake_body[0] += 10

    #print(snake_position)
    snake_position.insert(0,snake_temp)

    window.fill(0)
    for pos in snake_position:
        pygame.draw.rect(window,(0,255,0), pygame.Rect(pos[0], pos[1], 10, 10))
    #print(fruitpos[0:1])
    
    pygame.draw.rect(window,[0,255,255],fruitpos)
    pygame.draw.rect(window,[0,255,255],ruitpos)
    window.blit(text,(0,0))

    if snake_position[0][0]==fruitpos[0] and snake_position[0][1]==fruitpos[1]:     
        score +=1
        temp +=1
        fruitpos[0]=randint(1,108)*10
        fruitpos[1]=randint(1,90)*10
        
        
    if snake_position[0][0]==ruitpos[0] and snake_position[0][1]==ruitpos[1]:     
        score +=1
        temp +=1    
        ruitpos[0]=randint(1,108)*10
        ruitpos[1]=randint(1,90)*10

    
    
    if not temp==1:
        temp=0
        snake_position.pop(-1)
    else:
        temp=0


    died = fonta.render("You died, your score was "+str(score),True,(255,0,0),0)
    for i in range(len(snake_position)-1):
        if snake_position[0][0]==snake_position[i+1][0] and snake_position[0][1]==snake_position[i+1][1]:
            die()


    
    if snake_position[0][0]>1080 or snake_position[0][1]>900:  
        die()

    if snake_position[0][0]<0 or snake_position[0][1]<0:
        die()
        

    pygame.display.update()
    

pygame.quit()
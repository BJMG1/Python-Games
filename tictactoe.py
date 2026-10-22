import pygame

pygame.init()
screen=pygame.display.set_mode((900,900))
global saved
saved=[]

def x(x,y):
    pygame.draw.rect(screen,(255,0,255),(x-150,y,300,5))
    pygame.draw.rect(screen,(255,0,255),(x,y-150,5,300))

def o(x,y):
    pygame.draw.circle(screen,(255,255,255),(x,y),150)


def win(player):
    screen.fill((0,0,0))
    font = pygame.font.SysFont("Arial", 100)
    text = font.render(f"Player {player} wins!", True, (255, 255, 255))
    screen.blit(text, (100, 400))
    pygame.display.update()
    pygame.time.delay(3000)



def checkwin():
    if g[0,0]==g[0,1]==g[0,2] and g[0,0] == 1:
        print("Player X wins!")
        win("X")
    elif g[0,0]==g[1,1]==g[2,2] and g[0,0] == 1:
        print("Player X wins!")
        win("X")
    elif g[0,2]==g[1,1]==g[2,0] and g[0,2] == 1:
        print("Player X wins!")
        win("X")
    elif g[1,0]==g[1,1]==g[1,2] and g[1,0] == 1:
        print("Player X wins!")
        win("X")
    elif g[2,0]==g[2,1]==g[2,2] and g[2,0] == 1:
        print("Player X wins!")
        win("X")
    elif g[0,1]==g[1,1]==g[2,1] and g[0,1] == 1:
        print("Player X wins!")
        win("X")
    elif g[0,0]==g[1,0]==g[2,0] and g[0,0] == 1:
        print("Player X wins!")
        win("X")
    elif g[2,0]==g[2,1]==g[2,2] and g[2,0] == 1:
        print("Player x wins!")
        win("X")

    if g[0,0]==g[0,1]==g[0,2] and g[0,0] == 0:
        print("Player O wins!")
        win("O")
    elif g[0,0]==g[1,1]==g[2,2] and g[0,0] == 0:
        print("Player O wins!")
        win("O")
    elif g[0,2]==g[1,1]==g[2,0] and g[0,2] == 0:
        print("Player O wins!")
        win("O")
    elif g[1,0]==g[1,1]==g[1,2] and g[1,0] == 0:
        print("Player O wins!")
        win("O")
    elif g[2,0]==g[2,1]==g[2,2] and g[2,0] == 0:
        print("Player O wins!")
        win("O")
    elif g[0,1]==g[1,1]==g[2,1] and g[0,1] == 0:
        print("Player O wins!")
        win("O")
    elif g[0,0]==g[1,0]==g[2,0] and g[0,0] == 0:
        print("Player O wins!")
        win("O")
    elif g[2,0]==g[2,1]==g[2,2] and g[2,0] == 0:
        print("Player O wins!")
        win("O")


g={}
for y in range(3):
        for h in range(3):
            g[h,y] = -1

cursurvalue=0
while True:
    screen.fill((0,0,0))
    pygame.draw.line(screen,(255,255,255),(300,0),(300,900),5)
    pygame.draw.line(screen,(255,255,255),(600,0),(600,900),5)
    pygame.draw.line(screen,(255,255,255),(0,300),(900,300),5)
    pygame.draw.line(screen,(255,255,255),(0,600),(900,600),5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cursurvalue==1:
                cursurvalue=0
            else:
                cursurvalue=1
            pos=pygame.mouse.get_pos()
            print(pos)
            if pos[0]<300 and pos[1]<300:
                g[0,0]=cursurvalue
            elif pos[0]<600 and pos[1]<300:
                g[0,1]=cursurvalue
            elif pos[0]<900 and pos[1]<300:
                g[0,2]=cursurvalue
            elif pos[0]<300 and pos[1]<600:
                g[1,0]=cursurvalue
            elif pos[0]<600 and pos[1]<600:
                g[1,1]=cursurvalue
            elif pos[0]<900 and pos[1]<600:
                g[1,2]=cursurvalue
            elif pos[0]<300 and pos[1]<900:
               g[2,0]=cursurvalue
            elif pos[0]<600 and pos[1]<900:
                g[2,1]=cursurvalue
            elif pos[0]<900 and pos[1]<900:
                g[2,2]=cursurvalue

    pygame.time.delay(100)
    for i in g:
        if g[i]==1:
            x((i[1]*300)+150,(i[0]*300)+150)
        if g[i]==0:
            o((i[1]*300)+150,(i[0]*300)+150)

    checkwin()
    pygame.display.update()


    
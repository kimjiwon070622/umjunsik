import pygame
pygame.init()

size= [500,900]
screen=pygame.display.set_mode(size)
title="HANGMAN"
pygame.display.set_caption(title)

clock=pygame.time.Clock()
black=(255,255,255)
white=(0,0,0)
red=(255,0,0)
h_font=pygame.font.Font("C:/Windows/Fonts/ariblk.ttf",80)
e_font=pygame.font.Font("C:/Windows/Fonts/ariblk.ttf",50)


def tup_r(tup):
    temp_list=[] 
    for a in tup:
        temp_list.append(round(a))
    return tuple(temp_list)
k=0
try_num=0
drop=False
exit=False
e_text=" "
while not exit:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True
        if event.type==pygame.KEYDOWN:
            key_name=pygame.key.name(event.key)
            e_text=key_name

    k=k+1
    screen.fill(white)
    A=tup_r((0,size[1]*2/3))
    B=(size[0],A[1])
    pygame.draw.line(screen, black,A,B,3)
    C=(size[0]/6,A[1])
    D=(C[0],C[0])
    pygame.draw.line(screen, black,C,D,3)
    E=tup_r((size[0]/2,D[1]))   
    pygame.draw.line(screen, black,D,E,3)
    F=(E[0],E[1]+C[0])

    if drop==False:
        pygame.draw.line(screen, black,E,F,3)
    head=round(size[0]/12)
    if drop==True:
        G=(F[0],F[1]+head+k*5)
    else:
        G=(F[0],F[1]+head)

    pygame.draw.circle(screen, black,G,head,3)
    H=(G[0],G[1]+head)
    I=(H[0],H[1]+head/2)
    pygame.draw.line(screen, black,I,H,3)
    J=(I[0],I[1]+head*2)
    pygame.draw.line(screen, black,I,J,3)
    K=(J[0]-head,I[1]+head)
    pygame.draw.line(screen, black,I,K,3)
    L=(J[0]+head,K[1])
    pygame.draw.line(screen, black,I,L,3)
    M=(J[0]-head,J[1]+head)
    pygame.draw.line(screen, black,J,M,3)
    N=(J[0]+head,M[1])
    pygame.draw.line(screen, black,J,N,3)

    if drop==False and try_num==8:
        O=(F[0]-C[0], F[1])
        P=(O[0]+k*2, O[1])
        if P[0]>=E[0]+C[0]:
            drop=True
            k=0
        pygame.draw.line(screen, red,O,P,3)

    show="_ _ _ _"
    hint=h_font.render(show, True, black)
    h_size=hint.get_size()
    h_pos=tup_r((size[0]/2-h_size[0]/2, size[1]*5/6-h_size[1]/2))
    screen.blit(hint, h_pos)

    entry=e_font.render(e_text,True,white)
    e_size=entry.get_size()
    e_pos=tup_r((size[0]/2-e_size[0]/2,size[1]*17/18-e_size[1]/3))
    e_bg_size=80
    pygame.draw.rect(screen,black,(size[0]/2-e_bg_size/2, size[1]-e_bg_size, e_bg_size, e_bg_size))
    screen.blit(entry, e_pos)

    pygame.display.flip()
pygame.QUIT()

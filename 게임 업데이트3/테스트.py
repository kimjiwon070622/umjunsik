import pygame, math
pygame.init()
size = (500,900)
screen = pygame.display.set_mode(size)
title = '엄'
pygame.display.set_caption(title)
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)

def tup_r(tup):
    temp_list = []
    for a in tup:
        temp_list.append(round(a))
    return tuple(temp_list)
# 4
exit = False
while not exit:
# 4 - 1
    clock.tick(60)
# 4 - 2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
# 4 - 3
# 4 - 4 
        screen.fill(white)
        A = tup_r((0,size[1]*2/3))
        B = (size[0],A[1])
        C = (size[0]/6,A[1])
        D = (C[0],C[0])
        E = (size[0]/2,D[1])
        F = tup_r((E[0],E[1]+C[0]))

        
    
        pygame.draw.line(screen, black, A,B,3)
        pygame.draw.line(screen, black, C,D,3)
        pygame.draw.line(screen, black, D,E,3)
        pygame.draw.line(screen, black, E,F,3) 
        r_head=round(size[0]/12)
        G = (F[0],F[1]+r_head)
        pygame.draw.circle(screen,black, G, r_head, 3)
        H = (G[0],G[1]+r_head)
        I = (H[0],H[1]+r_head/2)
        J = (H[0],I[1]+r_head*2)
        K = (J[0] - r_head,I[1]+r_head)
        L = (J[0] + r_head,I[1]+r_head)
        M = (J[0] - r_head,J[1]+r_head)
        N = (J[0] + r_head,J[1]+r_head)
        pygame.draw.line(screen, black, I,H,3)
        pygame.draw.line(screen, black, I,J,3)
        pygame.draw.line(screen, black, I,L,3)
        pygame.draw.line(screen, black, I,K,3)
        pygame.draw.line(screen, black, J,N,3)
        pygame.draw.line(screen, black, J,M,3)
        
#4-5. 업데이트
        pygame.display.flip()
#5. 게임종료
pygame.QUIT()
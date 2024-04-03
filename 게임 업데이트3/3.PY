import pygame, math
#1. 게임초기화
pygame.init()
#2. 게임창 옵션 설정
size =[500,900]
screen = pygame.display.set_mode(size)
title = "HANGMAN"
pygame.display.set_caption(title)
#3. 게임 내 필요한 설정
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
def tup_r(tup):
    temp_list=[]
    for a in tup:
        temp_list.append(round(a))
    return tuple(temp_list)
exit = False
#4. 메인 이벤트
while not exit:
#4-1. FPS 설정
    clock.tick(60)
#4-2. 입력감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
#4-3. 입력이나 시간에 따른 변화
#4-4. 그리기
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
        I = (H[0],H[1]+r_head)

        pygame.draw.line(screen, black, I,H,3)
        pygame.draw.line(screen, black, H,I,3)
        I_arm=r_head*2
        J=tup_r((I[0]-I_arm*math.cos(30*math.pi/180),I[1]+I_arm*math.sin(30*math.pi/180)))
        pygame.draw.line(screen, black, I,J,3)
        I_arm=r_head*2
        K=tup_r((I[0]-I_arm*math.sin(30*math.pi/180),I[1]+I_arm*math.cos(30*math.pi/180)))
        pygame.draw.line(screen, black, I,K,3) 
        pygame.draw.line(screen, black, I,H,3)

#4-5. 업데이트
        pygame.display.flip()
#5. 게임종료
pygame.QUIT()

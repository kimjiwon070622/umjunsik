import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 크기 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("1인용 탁구게임")
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 1)

# 색상 및 글꼴 설정
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
large_font = pygame.font.SysFont('malgungothic', 72)
small_font = pygame.font.SysFont('malgungothic', 36)

# 변수 초기화
p1_score = 0
p2_score = 0
P1_WIN = 1
P2_WIN = 2
game_over = 0

ball = pygame.Rect(SCREEN_WIDTH // 2 - 16 // 2, SCREEN_HEIGHT // 2 - 16 // 2, 16, 16)
ball_dx = 5
ball_dy = -5

p1_paddle = pygame.Rect(0, SCREEN_HEIGHT // 2 - 80 // 2, 35, 250)
p2_paddle = pygame.Rect(SCREEN_WIDTH - 15, SCREEN_HEIGHT // 2 - 80 // 2, 16, 80)
p2_paddle_dy = 0

# 난이도 설정 변수
difficulty = None
easy_speed = 5
medium_speed = 7
hard_speed = 10

# 대시 설정 변수
dash_time = 250  # 대시로 인식할 시간 간격 (밀리초)
last_ctrl_press = 0
last_alt_press = 0
dash_distance = 100

# 사운드 초기화
try:
    pygame.mixer.init()
    pygame.mixer.music.load('music.mp3')  # 배경 음악 파일 경로 확인
    pygame.mixer.music.play(-1)  # -1: 무한 반복
    bounce_sound = pygame.mixer.Sound('파카후잉.mp3')  # 사운드 파일 경로 확인
    p1_win_sound = pygame.mixer.Sound('야미.mp3')
    p2_win_sound = pygame.mixer.Sound('짐.mp3')
except pygame.error as e:
    print(f"Error loading sound: {e}")

# 게임 루프
game_started = False
while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if not game_started:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    difficulty = 'easy'
                    ball_dx = easy_speed
                    ball_dy = -easy_speed
                elif event.key == pygame.K_x:
                    difficulty = 'medium'
                    ball_dx = medium_speed
                    ball_dy = -medium_speed
                elif event.key == pygame.K_c:
                    difficulty = 'hard'
                    ball_dx = hard_speed
                    ball_dy = -hard_speed
                elif event.key == pygame.K_SPACE and difficulty:
                    game_started = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                p1_paddle.top -= 1 # 패들 이동 속도 증가(위치조정)
            elif event.key == pygame.K_DOWN:
                p1_paddle.top += 1
            if event.key == pygame.K_LCTRL:
                current_time = pygame.time.get_ticks()
                if current_time - last_ctrl_press < dash_time:
                    p1_paddle.top -= dash_distance  # 위로 대시
                else:
                    p1_paddle.top -= 10  # 패들 이동 속도 증가(위치조정)
                last_ctrl_press = current_time
            elif event.key == pygame.K_LALT:
                current_time = pygame.time.get_ticks()
                if current_time - last_alt_press < dash_time:
                    p1_paddle.top += dash_distance  # 아래로 대시
                else:
                    p1_paddle.top += 10  # 패들 이동 속도 증가(위치조정)
                last_alt_press = current_time

    if game_started:
        # 게임 진행 코드
        if game_over == 0:
            if p1_score >= 2:
                game_over = P1_WIN
                pygame.mixer.music.stop()
                p1_win_sound.play()

            if p2_score >= 5:
                game_over = P2_WIN
                pygame.mixer.music.stop()
                p2_win_sound.play()

            ball.left += ball_dx
            ball.top += ball_dy

            if ball.left < 0:
                p2_score += 1
                ball.centerx = SCREEN_WIDTH // 2
                ball.centery = SCREEN_HEIGHT // 2
                ball_dx = abs(ball_dx)
                ball_dy = -abs(ball_dy)
            elif ball.right > SCREEN_WIDTH:
                p1_score += 1
                ball.centerx = SCREEN_WIDTH // 2
                ball.centery = SCREEN_HEIGHT // 2
                ball_dx = -abs(ball_dx)
                ball_dy = -abs(ball_dy)
            if ball.top < 0 or ball.bottom > SCREEN_HEIGHT:
                ball_dy *= -1
                bounce_sound.play()

            if p2_paddle.centery < ball.centery:
                p2_paddle_dy = ball_dx
            elif p2_paddle.centery > ball.centery:
                p2_paddle_dy = -ball_dx
            else:
                p2_paddle_dy = 0

            p2_paddle.top += p2_paddle_dy

            if p1_paddle.top < 0:
                p1_paddle.top = 0
            elif p1_paddle.bottom > SCREEN_HEIGHT:
                p1_paddle.bottom = SCREEN_HEIGHT

            if p2_paddle.top < 0:
                p2_paddle.top = 0
            elif p2_paddle.bottom > SCREEN_HEIGHT:
                p2_paddle.bottom = SCREEN_HEIGHT

            if ball.colliderect(p1_paddle):
                ball_dx = ball_dx * -1.1
                if ball.centery <= p1_paddle.top or ball.centery > p1_paddle.bottom:
                    ball_dy = ball_dy * -1.1
                p1_paddle.height -= 10
                if p1_paddle.height < 50:
                    p1_paddle.height = 50
                bounce_sound.play()

            if ball.colliderect(p2_paddle):
                ball_dx = ball_dx * -1.1
                if ball.centery <= p2_paddle.top or ball.centery > p2_paddle.bottom:
                    ball_dy = ball_dy * -1.1
                bounce_sound.play()

        if game_over == 0:
            pygame.draw.circle(screen, WHITE, (ball.centerx, ball.centery), ball.width // 2)

        pygame.draw.rect(screen, BLUE, p1_paddle)
        pygame.draw.rect(screen, BLUE, p2_paddle)

        p5_score_image = small_font.render('2점따면 승 AI는 5점따면 승 ', True, YELLOW)
        screen.blit(p5_score_image, (155, 50))

        p1_score_image = small_font.render('나 {}점'.format(p1_score), True, YELLOW)
        screen.blit(p1_score_image, (10, 10))

        p2_score_image = small_font.render('AI {}점'.format(p2_score), True, YELLOW)
        screen.blit(p2_score_image, p2_score_image.get_rect(right=SCREEN_WIDTH - 10, top=10))

        if game_over > 0:
            if game_over == P1_WIN:
                p1_win_image = large_font.render('내가 승', True, RED)
                screen.blit(p1_win_image, p1_win_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))
            elif game_over == P2_WIN:
                p2_win_image = large_font.render('AI 승', True, RED)
                screen.blit(p2_win_image, p2_win_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))

    else:
        # 난이도 선택 및 게임 시작 전 메시지 표시
        if not difficulty:
            select_difficulty_message = small_font.render('난이도를 선택하세요: Z-초, X-중, C-고', True, WHITE)
            screen.blit(select_difficulty_message, select_difficulty_message.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)))
        else:
            start_message = small_font.render('스페이스바를 눌러 게임 시작', True, WHITE)
            screen.blit(start_message, start_message.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))

        # 게임 설명 메시지 추가
        instruction_message = small_font.render('컨트롤: 위로 대쉬, 알트: 아래로 대쉬', True, WHITE)
        screen.blit(instruction_message, instruction_message.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)))
        move_message = small_font.render('화살표 키: 패들 이동', True, WHITE)
        screen.blit(move_message, move_message.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)))

    pygame.display.update()
    clock.tick(30)
pygame.quit()
sys.exit()

    